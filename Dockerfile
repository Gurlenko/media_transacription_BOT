
FROM python:3.12-slim


RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY environments.txt ./
COPY .env ./


RUN pip install --no-cache-dir -r environments.txt


COPY . .


RUN mkdir -p /tmp/whisper_bot


CMD ["python", "main.py"]
