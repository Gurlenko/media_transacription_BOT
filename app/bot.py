from aiogram import Bot, Dispatcher
from app.handlers.audio import router as audio_router
from app.handlers.video import router as video_router

def create_bot(token: str):
    bot = Bot(token)
    dp = Dispatcher()

    dp.include_router(audio_router)
    dp.include_router(video_router)

    return bot, dp
