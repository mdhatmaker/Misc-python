from bs4 import BeautifulSoup
from pytube import YouTube
import urllib.request
import time
import os


# https://stackoverflow.com/questions/59135180/keyerror-url-encoded-fmt-stream-map
# https://github.com/nficano/pytube/pull/534/commits/e5f1a9e2476b096ed2012939d50851d3499016e1


## list of link parsed by bs4
s = []


## to name and save the playlist folder and download path respectively 
directory = 'Hacker101'
savePath = "D:/Users/mhatm/Downloads/video/"
path = os.path.join(savePath, directory)


## link parser
past_link_here = "https://www.youtube.com/playlist?list=PLxhvVyxYRviZd1oEA9nmnilY3PhVrt4nj"
html_page = urllib.request.urlopen(past_link_here)
x = html_page.read()
soup = BeautifulSoup(x, 'html.parser')
for link in soup.findAll('a'):
    k = link.get('href')
    if 'watch' in k:
        s.append(k)
    else:
        pass


## to create playlist folder
def create_project_dir(x):
    if not os.path.exists(x):
        print('Creating directory ' + x)
        os.makedirs(x)
create_project_dir(path)


## downloading videos by using links from list s = []
for x in s:
    link="https://www.youtube.com" + x
    yt = YouTube(link)
    k = yt.title
    file_path = path + '\\' + k + '.mp4'
    try:
        if os.path.exists(file_path):
            print(k + ' is \n' + "already downloaded")
        else:
            j = yt.streams.filter(progressive=True).all()
            l = yt.streams.first()
            print(k + ' is downloading....')
            l.download(path)
            time.sleep(1)
            print('downloading compleat')

##    except Exception:
##        print('error')

    except KeyError as e:
        print('KeyError') % str(e)