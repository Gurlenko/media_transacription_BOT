import subprocess

def extract_audio(video_path: str) -> str:
    audio_path = f"{video_path}.wav"

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", video_path,
            "-ar", "16000",
            "-ac", "1",
            audio_path
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    return audio_path
