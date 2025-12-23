import logging
from faster_whisper import WhisperModel
from app.config import settings

logger = logging.getLogger(__name__)

logger.info(
    "Loading Whisper model=%s device=%s language=%s",
    settings.WHISPER_MODEL,
    settings.WHISPER_DEVICE,
    settings.WHISPER_LANGUAGE,
)

model = WhisperModel(
    settings.WHISPER_MODEL,
    device=settings.WHISPER_DEVICE,
    compute_type=settings.WHISPER_COMPUTE_TYPE,
)

def _transcribe(audio_path: str, language: str | None) -> str:
    segments, _ = model.transcribe(
        audio_path,
        beam_size=5,
        language=language,
    )
    return "".join(s.text for s in segments).strip()

def transcribe(audio_path: str) -> str:
    text = _transcribe(audio_path, settings.WHISPER_LANGUAGE)

    if not text or len(text) < 5:
        logger.info("Fallback to auto language detection")
        text = _transcribe(audio_path, None)

    return text
