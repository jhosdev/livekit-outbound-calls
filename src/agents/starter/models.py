from attr import define
from livekit.plugins import silero


@define
class UserData:
    vad: silero.VAD

@define
class ModelMetadata:
    user_name: str
    age: int
