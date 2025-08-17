from livekit.plugins import cartesia, deepgram, openai

from utils.environment import get_config

config = get_config()
config.check_required_env_vars()

agent_name = "lyra"
agent_instructions = """
You are a helpful voice AI assistant.
"""

agent_llm = openai.LLM(model="gpt-4o")
agent_stt = deepgram.STT(model="nova-3", language="multi")
agent_tts = cartesia.TTS(voice="12717d4c-6831-4b91-a0ab-e99d51755b10")
