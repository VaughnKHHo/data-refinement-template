from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    """Global settings configuration using environment variables"""

    INPUT_DIR: str = Field(
        default="/input",
        description="Directory containing input files to process"
    )

    OUTPUT_DIR: str = Field(
        default="/output",
        description="Directory where output files will be written"
    )

    REFINEMENT_ENCRYPTION_KEY: str = Field(
        default="0x043b9d76c6d25f536785c058ce788d8f441c9beff18538a864e2b9b3fcfbb3548c2d3c663907227ce90a3df9837e741d3995bae88b8f912de1a9c906bd02965d53",
        description="Key to symmetrically encrypt the refinement. This is derived from the original file encryption key"
    )

    # PINATA_API_KEY: Optional[str] = Field(
    #     default=None,
    #     description="Pinata API key"
    # )

    # PINATA_API_SECRET: Optional[str] = Field(
    #     default=None,
    #     description="Pinata API secret"
    # )

    PINATA_API_JWT: Optional[str] = Field(
        default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJkOGNjODFiNS04YzljLTQ2NWQtOThkMC1jZTBlZmE3MTliMmQiLCJlbWFpbCI6InZhdWdobkBwb2xpY3lkb2NrLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiIwMmVhMGI0MmU4OTYyZjBiMzgyZCIsInNjb3BlZEtleVNlY3JldCI6ImRhMDZhNGJmMTE2ODA0ZTgyYWRkZjJmMjYxOGFhMDYzMzFlMDZmMWVjNjcwNzIyZGI3ZDI5OTI5MjRkOTgyZWUiLCJleHAiOjE3Nzk3ODgzNDd9.EqBAIcdJZRUTIY8CRfl_uRCunhHV1nbg8E7AqG8lMQc",
        description="Pinata API JWT"
    )

    SCHEMA_NAME: str = Field(
        default="Telegram Chats",
        description="Name of the schema"
    )

    SCHEMA_VERSION: str = Field(
        default="1.0.0",
        description="Version of the schema"
    )

    SCHEMA_DESCRIPTION: str = Field(
        default="Schema for dFusion Social Truth DLP Telegram chats",
        description="Description of the schema"
    )

    SCHEMA_DIALECT: str = Field(
        default="sqlite",
        description="Dialect of the schema"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()