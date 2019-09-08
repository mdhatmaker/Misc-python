from pytube import YouTube

YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()

yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams.filter(progressive=True, file_extension='mp4')\
    .order_by('resolution')\
    .desc()\
    .first()\
    .download()