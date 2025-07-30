from typing import Literal

from attrs import define


@define
class AgentSession:
    llm: str
    stt: str
    tts: str
    stt_language: Literal["multi", "es", "en"] = "multi"

@define
class AgentConfig:
    instructions: str

