from __future__ import unicode_literals
import sys
from pytube import YouTube
import youtube_dl 


# https://www.tutorialspoint.com/python-library-pytube-to-download-youtube-videos
# https://stackoverflow.com/questions/40713268/download-youtube-video-using-python-to-a-certain-directory
# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')



if __name__ == "__main__":
    #url = "https://www.youtube.com/watch?v=n06H7OcPd-g"
    #url = "https://www.youtube.com/watch?v=kav3AqOE5t4"
    #url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    url = "https://www.youtube.com/watch?v=eLNd7-_XmtM"

    # using youtube-dl library
    # sudo -H pip install --upgrade youtube-dl
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    """ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])"""


    exit(0)


    # using pytube library
    yt = YouTube(url)
    #yt = yt.get('mp4', '720p')
    #yt.download('/path/to/download/directory')
    print(yt.title)
    #print(yt.thumbnail_url)
    #print(yt.streams.all())
    stream = yt.streams.first()
    print(stream)
    stream.download('D:\\Users\\mhatm\\Downloads')
