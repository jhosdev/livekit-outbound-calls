import logging
import os
from functools import lru_cache

import attrs

logger = logging.getLogger(__name__)


def _load_dotenv_if_local() -> None:
    """Load .env file if ENV is set to 'local'."""
    if os.getenv("ENV", "local") == "local":
        try:
            from dotenv import load_dotenv

            logger.info("Loading .env.local file")
            load_dotenv(".env.local")
        except ImportError:
            logger.warning("dotenv not found, skipping .env file loading")


@attrs.define(frozen=True)
class Config:
    """Application configuration loaded from environment variables."""

    # Environment
    env: str = attrs.field(factory=lambda: os.getenv("ENV", "local"), metadata={"required": False})

    # LiveKit - Real-time Media Infrastructure
    livekit_api_key: str = attrs.field(
        factory=lambda: os.getenv("LIVEKIT_API_KEY", ""), metadata={"required": True}
    )
    livekit_api_secret: str = attrs.field(
        factory=lambda: os.getenv("LIVEKIT_API_SECRET", ""), metadata={"required": True}
    )
    livekit_url: str = attrs.field(
        factory=lambda: os.getenv("LIVEKIT_URL", ""), metadata={"required": True}
    )

    # Deepgram - Speech-to-Text
    deepgram_api_key: str = attrs.field(
        factory=lambda: os.getenv("DEEPGRAM_API_KEY", ""), metadata={"required": True}
    )

    # OpenAI - Language Model
    openai_api_key: str = attrs.field(
        factory=lambda: os.getenv("OPENAI_API_KEY", ""), metadata={"required": True}
    )

    # Google - Language Model
    google_api_key: str = attrs.field(
        factory=lambda: os.getenv("GOOGLE_API_KEY", ""), metadata={"required": True}
    )

    # Cartesia - Text-to-Speech
    cartesia_api_key: str = attrs.field(
        factory=lambda: os.getenv("CARTESIA_API_KEY", ""), metadata={"required": True}
    )

    # Twilio/LiveKit - Telephony Infrastructure
    sip_outbound_trunk_id: str = attrs.field(
        factory=lambda: os.getenv("SIP_OUTBOUND_TRUNK_ID", ""), metadata={"required": True}
    )
    phone_number: str = attrs.field(
        factory=lambda: os.getenv("PHONE_NUMBER", ""), metadata={"required": True}
    )

    # MCP Server
    mcp_server_url:str = attrs.field(
        factory=lambda: os.getenv("MCP_URL", ""), metadata={"required": True}
    )
    mcp_server_header:str = attrs.field(
        factory=lambda: os.getenv("MCP_HEADER", ""), metadata={"required": True}
    )
    mcp_server_token:str = attrs.field(
        factory=lambda: os.getenv("MCP_TOKEN", ""), metadata={"required": True}
    )

    # Typesense - Search
    typesense_url: str = attrs.field(
        factory=lambda: os.getenv("TYPESENSE_URL", ""), metadata={"required": True}
    )
    typesense_api_key: str = attrs.field(
        factory=lambda: os.getenv("TYPESENSE_API_KEY", ""), metadata={"required": True}
    )

    # Postgres - Database

    def __attrs_post_init__(self) -> None:
        """Validate required configuration after initialization."""
        self.validate_required_keys()

    def validate_required_keys(self) -> None:
        """Validate that all required configuration keys are present and non-empty."""
        missing_keys: list[str] = []

        for field in attrs.fields(self.__class__):
            if field.metadata.get("required", False):
                value = getattr(self, field.name)
                if not value:
                    # Convert field name to environment variable name
                    env_var_name = field.name.upper()
                    missing_keys.append(env_var_name)

        if missing_keys:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_keys)}")

    @classmethod
    def check_required_env_vars(cls) -> list[str]:
        """
        Check which required environment variables are missing without creating a Config instance.

        Returns:
            List of missing environment variable names. Empty list if all are present.
        """
        missing_keys: list[str] = []

        for field in attrs.fields(cls):
            if field.metadata.get("required", False):
                env_var_name = field.name.upper()
                value = os.getenv(env_var_name, "")
                if not value:
                    missing_keys.append(env_var_name)

        return missing_keys

    @property
    def is_local(self) -> bool:
        """Check if running in local development environment."""
        return self.env == "local"

    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.env == "production"


@lru_cache(maxsize=1)
def get_config() -> Config:
    """
    Get the application configuration.

    Loads dotenv if ENV=local and returns a cached Config instance.
    This function is cached so config is only loaded once per application run.
    """
    _load_dotenv_if_local()
    return Config()


# Convenience export for easy importing
config = get_config()
