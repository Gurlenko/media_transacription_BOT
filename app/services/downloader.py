import os
from aiogram.types import Message
from app.config import settings
from app.utils.file_utils import ensure_dir

ensure_dir(settings.TMP_DIR)

async def download_file(message: Message) -> str:
    bot = message.bot
    file = (
        message.voice
        or message.audio
        or message.video
        or message.video_note
    )

    file_info = await bot.get_file(file.file_id)
    path = os.path.join(settings.TMP_DIR, file.file_id)

    await bot.download_file(file_info.file_path, path)
    return path
