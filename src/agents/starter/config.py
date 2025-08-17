from livekit.agents import mcp
from livekit.plugins import cartesia, deepgram, google

from utils.environment import get_config

config = get_config()
config.check_required_env_vars()

agent_name = "lyra"
agent_instructions = """
You are a helpful voice AI assistant.
"""

agent_llm = google.LLM(model="gemini-2.5-flash-preview-05-20")
agent_stt = deepgram.STT(model="nova-3", language="multi")
agent_tts = cartesia.TTS(voice="12717d4c-6831-4b91-a0ab-e99d51755b10")

agent_mcp_server = mcp.MCPServerHTTP(
    url=config.mcp_server_url,
    headers={
        config.mcp_server_header: config.mcp_server_token,
    },
    timeout=10,
    client_session_timeout_seconds=10,
)
