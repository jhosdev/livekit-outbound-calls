import logging

from livekit.agents import Agent, ChatContext

from agents.starter.config import (
    agent_instructions,
    agent_llm,
    agent_stt,
    agent_tts,
)

logger = logging.getLogger(__name__)


class GreeterAgent(Agent):
    def __init__(self, chat_ctx: ChatContext) -> None:
        super().__init__(  # pyright: ignore[reportUnknownMemberType]
            llm=agent_llm,
            stt=agent_stt,
            tts=agent_tts,
            instructions=agent_instructions,
            chat_ctx=chat_ctx,
        )
