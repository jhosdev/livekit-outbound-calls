from pathlib import Path

from shared.config import AgentConfig, AgentSession

session_config = AgentSession(
    llm="gemini-2.5-flash-preview-05-20",
    stt="nova-3",
    tts="12717d4c-6831-4b91-a0ab-e99d51755b10",
    stt_language="multi",
)

agent_config = AgentConfig(
    instructions="""
    You are a helpful voice AI assistant.
    You eagerly assist users with their questions by providing information from your extensive knowledge.
    Your responses are concise, to the point, and without any complex formatting or punctuation.
    You are curious, friendly, and have a sense of humor.
    You talk in spanish.
    You assist users with programming questions
    """
)

agent_name = "base-agent"

(output_dir := Path(__file__).parent.parent.parent / "output").mkdir(parents=True, exist_ok=True)


def get_output_path(filename: str) -> Path:
    """Get the output path for a given filename."""
    return output_dir / filename
