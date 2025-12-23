from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass(frozen=True)
class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")

    WHISPER_MODEL: str = os.getenv("WHISPER_MODEL", "small")
    WHISPER_DEVICE: str = os.getenv("WHISPER_DEVICE", "cpu")
    WHISPER_COMPUTE_TYPE: str = os.getenv("WHISPER_COMPUTE_TYPE", "int8")
    WHISPER_LANGUAGE: str | None = os.getenv("WHISPER_LANGUAGE", "uk")

    TMP_DIR: str = os.getenv("TMP_DIR", "/tmp/whisper_bot")
    MAX_WORKERS: int = int(os.getenv("MAX_WORKERS", 4))

settings = Settings()
