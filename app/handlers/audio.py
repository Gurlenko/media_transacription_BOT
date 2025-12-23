import asyncio
from aiogram import Router, F
from aiogram.types import Message

from app.services.downloader import download_file
from app.services.transcriber import transcribe
from app.services.executor import executor

router = Router()

@router.message(F.voice | F.audio)
async def audio_handler(message: Message):
    loop = asyncio.get_running_loop()

    file_path = await download_file(message)

    text = await loop.run_in_executor(
        executor,
        transcribe,
        file_path
    )

    await message.answer(
        text or "Вилами по воді...",
        reply_to_message_id=message.message_id,
    )
