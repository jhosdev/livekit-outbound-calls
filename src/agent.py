import logging

from attr import define
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    RoomInputOptions,
    RoomOutputOptions,
    RunContext,
    WorkerOptions,
    cli,
    metrics,
)
from livekit.agents.llm import function_tool
from livekit.agents.voice import MetricsCollectedEvent
from livekit.plugins import cartesia, deepgram, google, noise_cancellation, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from utils.environment import get_config

get_config().check_required_env_vars()

logger = logging.getLogger("agent")


@define
class UserData:
    vad: silero.VAD


class BaseAgent(Agent):
    def __init__(self) -> None:
        super().__init__(  # pyright: ignore[reportUnknownMemberType]
            instructions="""You are a helpful voice AI assistant.
            You eagerly assist users with their questions by providing information from your extensive knowledge.
            Your responses are concise, to the point, and without any complex formatting or punctuation.
            You are curious, friendly, and have a sense of humor.""",
        )

    # all functions annotated with @function_tool will be passed to the LLM when this
    # agent is active
    @function_tool
    async def lookup_weather(self, _: RunContext[UserData], location: str):
        """Use this tool to look up current weather information in the given location.

        If the location is not supported by the weather service, the tool will indicate this. You must tell the user the location's weather is unavailable.

        Args:
            location: The location to look up weather information for (e.g. city name)
        """

        logger.info(f"Looking up weather for {location}")

        return "sunny with a temperature of 70 degrees."


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    # each log entry will include these fields
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    # Set up a voice AI pipeline using OpenAI, Cartesia, Deepgram, and the LiveKit turn detector
    session: AgentSession[UserData] = AgentSession(
        # any combination of STT, LLM, TTS, or realtime API can be used
        llm=google.LLM(model="gemini-2.5-flash-preview-05-20"),
        stt=deepgram.STT(model="nova-3", language="multi"),
        tts=cartesia.TTS(voice="6f84f4b8-58a2-430c-8c79-688dad597532"),
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

    await session.start(
        agent=BaseAgent(),
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


def main():
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))


if __name__ == "__main__":
    main()
