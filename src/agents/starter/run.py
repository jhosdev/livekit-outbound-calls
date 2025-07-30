import logging
from json import JSONDecodeError, loads

from livekit.agents import (
    AgentSession,
    ChatContext,
    JobContext,
    RoomInputOptions,
    RoomOutputOptions,
    WorkerOptions,
    cli,
    metrics,
)
from livekit.agents.voice import MetricsCollectedEvent
from livekit.plugins import cartesia, deepgram, google, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from agents.starter.agent import StarterAgent, prewarm
from agents.starter.config import session_config
from agents.starter.models import ModelMetadata, UserData

logger = logging.getLogger(__name__)

async def entrypoint(ctx: JobContext):
    # each log entry will include these fields
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }
    metadata_json = ctx.job.metadata
    print(ctx.job)
    logger.info(f"Received metadata: {metadata_json}")

    try:
        logger.debug("Parsing job metadata")
        print(metadata_json)
        metadata: ModelMetadata | None = loads(metadata_json)
    except JSONDecodeError:
        logger.warning("Failed to parse job metadata, using empty metadata")
        metadata = None

    # Set up a voice AI pipeline using OpenAI, Cartesia, Deepgram, and the LiveKit turn detector
    session: AgentSession[UserData] = AgentSession(
        # any combination of STT, LLM, TTS, or realtime API can be used
        llm=google.LLM(model=session_config.llm),
        stt=deepgram.STT(model=session_config.stt, language=session_config.stt_language),
        tts=cartesia.TTS(voice=session_config.tts),
        # use LiveKit's turn detection model
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
    )

    # To use the OpenAI Realtime API, use the following session setup instead:
    # session = AgentSession(
    #     llm=openai.realtime.RealtimeModel()
    # )

    # log metrics as they are emitted, and total usage after session is over
    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")  # pyright: ignore[reportUntypedFunctionDecorator, reportUnknownMemberType]
    def _on_metrics_collected(ev: MetricsCollectedEvent):  # pyright: ignore[reportUnusedFunction]
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    # shutdown callbacks are triggered when the session is over
    ctx.add_shutdown_callback(log_usage)

    initial_ctx = ChatContext()
    initial_ctx.add_message(
        role="assistant",
        content=f"The user information is: {metadata}"
    )

    await session.start(
        agent=StarterAgent(
            chat_ctx=initial_ctx
        ),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
        room_output_options=RoomOutputOptions(transcription_enabled=True),
    )

    # join the room when agent is ready
    await ctx.connect()

    await session.generate_reply(
        instructions="Greet the user by name and offer your assistance on programming paths."
    )


def main():
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm, agent_name="base-agent"))

if __name__ == "__main__":
    main()
