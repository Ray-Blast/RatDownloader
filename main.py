# Rat DOwnloader
# Created by Ray Blast

import downloader as dl

download_directory = "downloads"
test_url = "https://www.youtube.com/watch?v=_m9LHQjsGYM" #phonk lol

if __name__ == '__main__':
    dl.downloadVideo(test_url, download_directory)