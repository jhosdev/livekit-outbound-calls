import logging

from livekit.agents import Agent, ChatContext, JobProcess, RunContext, mcp
from livekit.agents.llm import function_tool
from livekit.plugins import silero

from agents.starter.config import (
    agent_instructions,
    agent_llm,
    agent_mcp_server,
    agent_name,
    agent_stt,
    agent_tts,
)
from agents.starter.models import UserData
from utils.environment import get_config

config = get_config()
config.check_required_env_vars()

logger = logging.getLogger(__name__)


class StarterAgent(Agent):
    def __init__(self, chat_ctx: ChatContext) -> None:
        super().__init__(  # pyright: ignore[reportUnknownMemberType]
            instructions=agent_config.instructions,
            chat_ctx=chat_ctx,
            mcp_servers=[
                mcp.MCPServerHTTP(
                    url=config.mcp_server_url,
                    headers={
                        config.mcp_server_header: config.mcp_server_token,
                    },
                    timeout=10,
                    client_session_timeout_seconds=10,
                ),
            ],
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
