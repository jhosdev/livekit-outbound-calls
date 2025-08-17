from livekit.agents import JobContext, JobProcess, WorkerOptions, cli
from livekit.agents.voice import AgentSession
from livekit.plugins import silero

from shared.config import SessionInfo


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()

async def entrypoint(ctx: JobContext):
    session_info = SessionInfo(
        {
            "greeter":
        }
    )
    session = AgentSession[SessionInfo](
        userdata=session_info,
    )

    await session.start(
        agent=session_info.agents.get("main"),
    )

if __name__ == "__main__":
    cli.run_app(WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm,
        )
    )
