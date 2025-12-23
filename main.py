import asyncio
from app.bot import create_bot
from app.config import settings
from app.logging import setup_logging

async def main():
    setup_logging()
    bot, dp = create_bot(settings.BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
