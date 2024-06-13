import subprocess
def downloadVideo(video_url: str, download_path: str):
    subprocess.run(f'yt-dlp {video_url} -P {download_path}\\Videos', shell=True)

def downloadPicture(picture_url: str):
    subprocess.run(f"gallery-dl {picture_url}")
