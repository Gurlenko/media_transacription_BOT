from concurrent.futures import ThreadPoolExecutor
from app.config import settings

executor = ThreadPoolExecutor(
    max_workers=settings.MAX_WORKERS
)
