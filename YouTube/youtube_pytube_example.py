from pytube import YouTube

# https://www.tutorialspoint.com/python-library-pytube-to-download-youtube-videos


"""
#url = "https://www.youtube.com/watch?v=eLNd7-_XmtM"
url = 'https://youtu.be/9bZkp7q19f0'
YouTube(url).streams.first().download()
"""

yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams.filter(progressive=True, file_extension='mp4')\
    .order_by('resolution')\
    .desc()\
    .first()\
    .download()