"""from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])"""


from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=n06H7OcPd-g")
#yt = yt.get('mp4', '720p')
#yt.download('/path/to/download/directory')
print(yt.title)
print(yt.thumbnail_url)
print(yt.streams.all())
stream = yt.streams.first()
stream.download('C:\\Users\\mhatm\\Downloads')
