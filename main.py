# Rat DOwnloader
# Created by Ray Blast

import downloader as dl

download_directory = "G:\\Videos\\yt-dlp-vids\\RatDownloader"
test_url = "https://www.youtube.com/watch?v=_m9LHQjsGYM" #phonk lol

user_url = ""

if __name__ == '__main__':
    user_url = input("Please enter the url you want to download: ")
    dl.downloadVideo(user_url, download_directory)