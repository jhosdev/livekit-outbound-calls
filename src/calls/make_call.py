import asyncio
import logging
import uuid
from json import dumps

from attrs import asdict
from livekit import api

from agents.starter.config import agent_name
from agents.starter.models import ModelMetadata
from utils.environment import get_config

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    #format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

config = get_config()
config.check_required_env_vars()

# Configuration
room_name_prefix = "survey-call-"
outbound_trunk_id = config.sip_outbound_trunk_id


async def make_survey_call(phone_number: str):
    """Create a dispatch and add a SIP participant to call the phone number with survey question"""
    # Create a unique room name for each call using the prefix and row index
    room_id = str(uuid.uuid4())
    logger.info(f"Generated unique room ID: {room_id}")
    room_name = f"{room_name_prefix}{room_id}"

    metadata = ModelMetadata(
        user_name="Jhosaim",
        age=30
    )

    # Create metadata as JSON containing all relevant data
    metadata_dump = dumps(asdict(metadata))
    logger.info(f"Metadata for dispatch: {metadata_dump}")

    lkapi = api.LiveKitAPI()

    logger.info(f"Creating dispatch for agent {agent_name} in room {room_name}")

    dispatch = await lkapi.agent_dispatch.create_dispatch(
        api.CreateAgentDispatchRequest(agent_name=agent_name, room=room_name, metadata=metadata_dump)
    )
    logger.info(f"Created dispatch: {dispatch}")
    logger.info(f"Dialing phone to room {room_name}")
    logger.info(f"Dispatches: {await lkapi.agent_dispatch.list_dispatch(room_name)}")

    sip_participant = await lkapi.sip.create_sip_participant(
        api.CreateSIPParticipantRequest(
            room_name=room_name,
            sip_trunk_id=outbound_trunk_id,
            sip_call_to=phone_number,
            participant_identity="phone_user",
        )
    )
    logger.info(f"Created SIP participant: {sip_participant}")

    await lkapi.aclose()
    return True


async def main():
    logger.info("Starting survey calls process")
    await make_survey_call(config.phone_number)
    logger.info("Survey calls process completed")


if __name__ == "__main__":
    asyncio.run(main())
