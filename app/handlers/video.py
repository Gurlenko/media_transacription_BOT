import asyncio
from aiogram import Router, F
from aiogram.types import Message

from app.services.downloader import download_file
from app.services.audio_extractor import extract_audio
from app.services.transcriber import transcribe
from app.services.executor import executor

router = Router()

@router.message(F.video | F.video_note)
async def video_handler(message: Message):
    loop = asyncio.get_running_loop()

    video_path = await download_file(message)
    audio_path = extract_audio(video_path)

    text = await loop.run_in_executor(
        executor,
        transcribe,
        audio_path
    )

    await message.answer(
        text or "З возу на стіл...",
        reply_to_message_id=message.message_id,
    )
