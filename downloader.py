import subprocess
def downloadVideo(video_url: str, download_path: str):
    try:

        subprocess.run(f'yt-dlp -f "bv*[vcodec^=avc]+ba[ext=m4a]/b[ext=mp4]/b" -S vcodec:h264,fps,res,acodec:m4a --recode mp4 {video_url} -P {download_path}\\RatDLVideos', shell=True)
    except:
        subprocess.run(f"gallery-dl {video_url}", shell=True)
def downloadPicture(picture_url: str):
    subprocess.run(f"gallery-dl {picture_url}")
