
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import urllib.request as urllib2
import sys
from PIL import Image
from os.path import join
import os
import requests
import re
import pyperclip
import logging
import queue
import threading
import concurrent.futures
import time
import random 
#import urllib2
#import requests


#---------------------------------------------------------------------------------------------------
output_dir = "/Users/michael/Downloads/scrape"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
#---------------------------------------------------------------------------------------------------



def download_image2(url, do_overwrite = True, prefix=""):
  try:
    if url is None: return
    filename = prefix + url.split('/')[-1]
    output_pathname = join(output_dir, filename)
    if do_overwrite or (os.path.exists(output_pathname) == False):
      print(f'{filename}  -->  {output_pathname}')
      #urllib2.urlretrieve(url, output_pathname)
      r = requests.get(url)
      with open(output_pathname, 'wb') as outfile:
        outfile.write(r.content)
    else:
      print(f'((( {filename}  -->  {output_pathname} )))' )
    return
  except FileNotFoundError as err:
    print(err)   # something wrong with local path
  except HTTPError as err:
    print(err)  # something wrong with url
  except:
    print(f"Error downloading image {url}")

def get_download_image(url):
    fd = urllib2.urlopen(url)
    im = Image.open(fd)
    #print im.size
    return im

def download_image(url, do_overwrite = True, prefix=""):
    if url is None: return
    im = get_download_image(url)
    filename = prefix + url.split('/')[-1]
    #print im.size
    output_pathname = join(output_dir, filename)
    if do_overwrite or (os.path.exists(output_pathname) == False):
      print(f'{filename}  -->  {output_pathname}')
      im.save(output_pathname)
    else:
      print(f'((( {filename}  -->  {output_pathname} )))' )
    return

def download_image_as(url, filename, do_overwrite = True, prefix=""):
    if url is None: return
    output_pathname = join(output_dir, filename)
    if do_overwrite or (os.path.exists(output_pathname) == False):
      print(f'{filename}  -->  {output_pathname}')
      im = get_download_image(url)
      im.save(output_pathname)
    else:
      print(f'((( {filename}  -->  {output_pathname} )))' )
    return

def get_tags(url, tag="img"):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    return soup.find_all(tag)

def get_images(url, do_print=False):
    img_tags = get_tags(url, 'img')
    imgs = {}
    for img in img_tags:
        if img['src'].lower().endswith(".jpg"):
            #print(img)
            try:
                src = img['src']
                if do_print:
                  print(src)
                im = get_download_image(src)
                #imgs.append(im)
                imgs[src] = im
            except:
                continue
    return imgs

def save_images(format_url, i1, i2, prefix=""):
    for i in range(i1, i2+1):
        url = format_url.format(i)
        #print url
        im = get_download_image(url)
        filename = prefix + url.split('/')[-1]
        #print im.size
        print(filename)
        im.save(join(output_dir, filename))
    return

def url_exists(url):
    r = requests.get(url, stream=True)
    if r.status_code == 200:    # TODO: Maybe < 400 is better?
        return True
    else:
        return False


#url = "https://www.girlsofdesire.org/galleries/isabelle-tan-in-the-open-air/"
#url = "http://www.nightdreambabe.com/natural-beauty-lily-xo"

#response = requests.get(url)
#soup = BeautifulSoup(response.content, "html.parser")

#print(soup.prettify())
#print(soup.title.string)
#print(soup.p)

#save_images("http://contenta.novojoy.com/playboy/0711/{0:0>2}.jpg", 0, 15, prefix="bethanie")
#save_images("http://content4.chickteases.com/metartmoney.com/1548/{0:0>2}.jpg", 0, 14, prefix="ariel_piper_fawn")
#save_images("http://content4.babeimpact.com/playboy-plus.com/4489/Barbi_Benton_{0:0>2}.jpg", 0, 17)
#save_images("https://content4.morazzia.com/met-art/0905/{0:0>2}.jpg", 0, 17, prefix="lena_anderson")
#save_images("http://contenta.pleasuregirl.net/digitaldesire.com/7393/{0:0>2}.jpg", 0, 15)
#save_images("http://content4.babeimpact.com/ftvgirls.com/4196/Brooke_{0:0>2}.jpg", 0, 14)
#save_images("http://content4.babeimpact.com/celebrityspanker.com/0251/Mia_Rosing_{0:0>2}.jpg", 0, 15)
    


#url = "https://motherless.com/GI02DE763?page=3"
def process_image_page(url, minx=50, miny=50):      # minx and miny set the minimum horiz and vert size for images you care about
  if url_exists(url) == False:
    return False
  print(f'[ {url} ]')
  images = get_images(url, False)
  # Loop through the images
  count = 0
  for src, im in images.items():
    if im.size[0]>minx and im.size[1]>miny:
      count += 1
      print(f'{im.size}   {src}')
      download_image(src, False)
  print(f'>>> {count} images found ({len(images)} total)\n')
  if count > 1:
    return True
  else:
    return False

#base_url = "https://motherless.com/GI02DE763"
def process_image_pages(base_url, max_page=1000):
  if process_image_page(base_url):
    for i in range(2,max_page):
      url = f"{base_url}?page={i}"
      if process_image_page(url) == False:
        break
  return

#<a href="/G02DE763/1AE42A2" title="Unsorted Sexiness 33" class="caption title pop plain">Unsorted Sexiness 33</a>
def process_big_image_page(url):
  print(f'-------- {url}')
  #processed = {}
  a_tags = get_tags(url, 'a')
  for a in a_tags:
    try:
      href = a['href']
      p = re.compile('/G[0-9a-zA-Z]*/[0-9a-zA-Z]*')
      if p.match(href):
        #/G3247CE8/301BE30
        print(f"[{href}] [{a['title']}] [{a['class']}]")
        length = len(url) - len(url.split('/')[-1]) - 1
        #length = url.find('/', 8)
        root_url = url[0:length]
        big_img_url = f'{root_url}{href}'
        # if big_img_url in processed.items():
        #   continue
        # else:
        download_big_image(big_img_url)
        #processed[big_img_url] = True
    except KeyError as e:
      continue
  return

#base_url = "https://motherless.com/GI02DE763"
def process_big_image_pages(base_url, max_page=1000):
  if process_big_image_page(base_url):
    for i in range(2,max_page):
      url = f"{base_url}?page={i}"
      if process_big_image_page(url) == False:
        break
  return

#<img src="https://cdn5-images.motherlessmedia.com/images/F745626.jpg" alt="88472AB.jpg" id="motherless-media-image">
def download_big_image(url):
  #processed = {}
  img_tags = get_tags(url, 'img')
  for img in img_tags:
    if ('id' in img.attrs) and (img['id'] == "motherless-media-image"):
      #print(f"[{img['id']}]  [{img['alt']}]  [{img['src']}]")
      alt = img['alt'].replace('/', '_')
      if (not alt.endswith(".jpg")) and (not alt.endswith(".png")):
        alt = alt + ".jpg"
      #if alt in processed:
      #  continue
      #else:
      download_image_as(img['src'], alt, False)
      #processed[alt] = True
  return

def get_smutty_image_from_url(url):
  try:
    response = requests.get(url)  #, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch the page (status_code {response.status_code})")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    return get_smutty_image_from_soup(soup)
  except:
    print(f'Error getting image from url: {url}')
    return ''
  
def get_smutty_image_from_soup(soup):
  image = soup.find("img", {"class": "yesPopunder image_perma_img inner_rounded"})
  if image is None:
     image = soup.find("img", {"class": "yesPopunder image_perma_img"})
  if image is None:
     image = soup.find("img", {"class": "yesPopunder"})
  if image == None:
     return ''
  else:
    src = f"https:{image['src']}"
    return src

def process_smutty_image_page(url):
  imgurls = []
  print(f"processing URL --> {url}")
  #headers={'User-Agent': 'Mozilla/5.0'}
  response = requests.get(url)  #, headers=headers)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return
  soup = BeautifulSoup(response.text, 'html.parser')
  imgurl = get_smutty_image_from_soup(soup)
  if imgurl == None or imgurl == '':
    print(f'Error getting image from soup: {url}')
  else:
    #imgurls.append(imgurl)
    download_image(imgurl)
    #related = soup.find("div", {"id": "smutty_related"})
    #swidgets = related.find_all("div", {"class": "swidget_float"})
    swidgets = soup.find_all("div", {"class": "swidget_float"})
    for el in swidgets:
      a = el.find("a", {"class": "landscape"})
      href = f"https://smutty.com{a['href']}"
      print(href)
      imgurl = get_smutty_image_from_url(href)
      print(imgurl)
      #imgurls.append(imgurl)
      download_image(imgurl)
  return

def get_image_urls_from_smutty_page(url):
  imgurls = []
  print(f"getting image URLs --> {url}")
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return imgurls
  soup = BeautifulSoup(response.text, 'html.parser')
  imgurl = get_smutty_image_from_soup(soup)
  imgurls.append(imgurl)
  swidgets = soup.find_all("div", {"class": "swidget_float"})
  for el in swidgets:
    try:
      a = el.find("a", {"class": "landscape"})
      href = f"https://smutty.com{a['href']}"
      imgurl = get_smutty_image_from_url(href)
      print(f"{href}     {imgurl}")
      imgurls.append(imgurl)
    except:
      print(f'Error getting image from url: {href}')
  return imgurls

def get_urls_from_smutty_page(url):
  urls = []
  print(f"getting URLs --> {url}")
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return urls
  soup = BeautifulSoup(response.text, 'html.parser')
  swidgets = soup.find_all("div", {"class": "swidget_float"})
  for el in swidgets:
    a = el.find("a", {"class": "landscape"})
    href = f"https://smutty.com{a['href']}"
    print(f"{href}")
    urls.append(href)
  return urls


def remove_list_duplicates(list):
   return [*set(list)]




##############################################################################################################
#https://www.hotgirl.world/g/0mj1qwm5.html/?page=5
def get_hotgirlworld_page_urls(_url, i1=1, i2=20):
  if "?page=" in _url:
    url_split = _url.split('/')[0:-1]
    base_url = '/'.join(url_split)
  elif _url.endswith('/'):
    base_url = _url[0:-1]
  else:
    base_url = _url

  deep_urls = []
  #if "?page=" in _url:
  for i in range(i1, i2):
    deep_urls.append(f"{base_url}/?page={i}") #https://www.hotgirl.world/g/0mj1qwm5.html/?page={i}")
  return deep_urls

def get_hotgirlworld_image_urls(url):
  imgurls = []
  print(f"getting image URLs --> {url}")
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return imgurls
  soup = BeautifulSoup(response.text, 'html.parser')
  #findtest = soup.find_all('a')
  #findtest2 = soup.find_all('li', {"class": "article__image-item"}) # col-12 col-sm-12"
  ulist = soup.find_all('li', {"class": "article__image-item"})
  for el in ulist:
    try:
      #a = el.find("a", {"class": "landscape"})
      a = el.find('a')
      imgurl = f"https://www.hotgirl.world{a['href']}"
      print(f"{url}     {imgurl}")
      imgurls.append(imgurl)
    except:
      print(f'Error getting image from url: {url}')
  return imgurls

def process_hotgirlworld_page_urls(_urls):
  _image_urls = []
  i = 0
  for url in _urls:
    i += 1
    print(f"========== {i} / {len(_urls)} ==========")
    imgurls = get_hotgirlworld_image_urls(url)
    _image_urls.extend(imgurls)
  _image_urls = remove_list_duplicates(_image_urls)
  print(f"\n{len(_image_urls)} distinct image URLs\n")
  prefix = ""
  i = 0
  for li in _image_urls:
    try:
      filename = prefix + li.split('/')[-1]
      output_pathname = join(output_dir, filename)
      if (os.path.exists(output_pathname) == False):
        i += 1
        print(f"{i}   {output_pathname}")
        download_image2(li)
      else:
        i += 1
        print(f"{i}   SKIP EXISTING   {output_pathname}")
    except:
      print(f'Error processing image url: {li}')
##############################################################################################################

##############################################################################################################
#https://www.pornpics.com/galleries/south-korean-babe-poses-completely-naked-before-putting-on-fishnets-24147030/
def get_pornpics_image_urls(url):
  imgurls = []
  print(f"getting image URLs --> {url}")
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return imgurls
  soup = BeautifulSoup(response.text, 'html.parser')
  ulist = soup.find_all('li', {"class": "thumbwook"})
  for el in ulist:
    try:
      #a = el.find("a", {"class": "landscape"})
      a = el.find('a')
      imgurl = a['href']  #f"https://www.hotgirl.world{a['href']}"
      print(f"{url}     {imgurl}")
      imgurls.append(imgurl)
    except:
      print(f'Error getting image from url: {url}')
  return imgurls

def process_pornpics_page_urls(_urls):
  _image_urls = []
  i = 0
  for url in _urls:
    i += 1
    print(f"========== {i} / {len(_urls)} ==========")
    imgurls = get_pornpics_image_urls(url)
    _image_urls.extend(imgurls)
  _image_urls = remove_list_duplicates(_image_urls)
  print(f"\n{len(_image_urls)} distinct image URLs\n")
  prefix = ""
  i = 0
  for li in _image_urls:
    try:
      filename = prefix + li.split('/')[-1]
      output_pathname = join(output_dir, filename)
      if (os.path.exists(output_pathname) == False):
        i += 1
        print(f"{i}   {output_pathname}")
        download_image2(li)
    except:
      print(f'Error processing image url: {li}')
##############################################################################################################

##############################################################################################################
#https://scandalplanet.com/kate-upton2/
def get_scandalplanet_image_urls(url):
  imgurls = []
  print(f"getting image URLs --> {url}")
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return imgurls
  soup = BeautifulSoup(response.text, 'html.parser')
  ulist = soup.find_all('dt', {"class": "gallery-icon portrait"})
  for el in ulist:
    try:
      #a = el.find("a", {"class": "landscape"})
      a = el.find('a')
      imgurl = a['href']  #f"https://www.hotgirl.world{a['href']}"
      print(f"{url}     {imgurl}")
      imgurls.append(imgurl)
    except:
      print(f'Error getting image from url: {url}')
  return imgurls

def get_scandalplanet_video_urls(url):
  videourls = []
  print(f"getting video URLs --> {url}")
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return videourls
  soup = BeautifulSoup(response.text, 'html.parser')
  ulist = soup.find_all('video', {"id": "video-post"})
  for el in ulist:
    try:
      #a = el.find("a", {"class": "landscape"})
      a = el.find('source')
      imgurl = a['src']
      print(f"{url}     {imgurl}")
      videourls.append(imgurl)
    except:
      print(f'Error getting video from url: {url}')
  return videourls

def process_scandalplanet_page_urls(_urls, include_video = True):
  _image_urls = []
  i = 0
  for url in _urls:
    i += 1
    print(f"========== {i} / {len(_urls)} ==========")
    imgurls = get_scandalplanet_image_urls(url)
    videourls = get_scandalplanet_video_urls(url) if include_video else []
    _image_urls.extend(imgurls)
    _image_urls.extend(videourls)
  _image_urls = remove_list_duplicates(_image_urls)
  url_count = len(_image_urls)
  print(f"\n  --- {url_count} DISTINCT IMAGE/VIDEO URLS ---\n")
  prefix = ""
  i = 0
  for li in _image_urls:
    try:
      filename = prefix + li.split('/')[-1]
      output_pathname = join(output_dir, filename)
      if (os.path.exists(output_pathname) == False):
        i += 1
        print(f"{i}/{url_count}   {output_pathname}")
        download_image2(li)
    except:
      print(f'Error processing image url: {li}')
##############################################################################################################

##############################################################################################################
#https://thefappeningblog.com/category/cailin-russo/
#https://thefappeningblog.com/cailin-russo-upskirt-7-pics-video/
def get_thefappeningblog_page_urls(_url):
  deep_urls = []
  print(f"getting page URLs --> {_url}")
  response = requests.get(_url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return deep_urls
  soup = BeautifulSoup(response.text, 'html.parser')
  ulist = soup.find_all('header', {"class": "entry-header"})
  for el in ulist:
    el2 = el.find('h1', {"class": "entry-title"})
    el3 = el2.find('a')
    pageurl = el3['href']
    print(f"  {pageurl}")
    deep_urls.append(pageurl)
  return deep_urls

def get_thefappeningblog_image_urls(url):
  imgurls = []
  print(f"getting image URLs --> {url}")
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return imgurls
  soup = BeautifulSoup(response.text, 'html.parser')
  ulist = soup.find_all('div', {"class": "entry-content"})
  for el in ulist:
    try:
      #a = el.find("a", {"class": "landscape"})
      #alist = el.find_all('img', {"class": "size-medium"})
      # Find elements with a specific class
      #alist = el.select('.size-medium')
      plist = el.find_all('p')
      for el2 in plist:
        alist = el2.find_all('a')
        for el3 in alist:
          imgurl = el3['href']
          if (imgurl.startswith('https://thefappeningblog.com/wp-content') or imgurl.startswith('https://thefappeningblog.com/cnt')) and imgurl.endswith('.jpg'):
            print(f"{url}     {imgurl}")
            imgurls.append(imgurl)
      alist = el.find_all('a')
      for el3 in alist:
        imgurl = el3['href']
        if (imgurl.startswith('https://thefappeningblog.com/wp-content') or imgurl.startswith('https://thefappeningblog.com/cnt')) and imgurl.endswith('.jpg'):
          print(f"{url}     {imgurl}")
          imgurls.append(imgurl)
    except:
      print(f'Error getting image from url: {url}')
  return imgurls

def get_thefappeningblog_video_urls(url):
  videourls = []
  print(f"getting video URLs --> {url}")
  # response = requests.get(url)
  # if response.status_code != 200:
  #     print(f"Failed to fetch the page (status_code {response.status_code})")
  #     return videourls
  # soup = BeautifulSoup(response.text, 'html.parser')
  # ulist = soup.find_all('video', {"id": "video-post"})
  # for el in ulist:
  #   try:
  #     #a = el.find("a", {"class": "landscape"})
  #     a = el.find('source')
  #     imgurl = a['src']
  #     print(f"{url}     {imgurl}")
  #     videourls.append(imgurl)
  #   except:
  #     print(f'Error getting video from url: {url}')
  return videourls

def process_thefappeningblog_page_urls(_urls, include_video = False):
  _image_urls = []
  i = 0
  for url in _urls:
    i += 1
    print(f"========== {i} / {len(_urls)} ==========")
    imgurls = get_thefappeningblog_image_urls(url)
    videourls = get_thefappeningblog_video_urls(url) if include_video else []
    _image_urls.extend(imgurls)
    _image_urls.extend(videourls)
  _image_urls = remove_list_duplicates(_image_urls)
  url_count = len(_image_urls)
  print(f"\n  --- {url_count} DISTINCT IMAGE/VIDEO URLS ---\n")
  prefix = ""
  i = 0
  for li in _image_urls:
    try:
      filename = prefix + li.split('/')[-1]
      output_pathname = join(output_dir, filename)
      if (os.path.exists(output_pathname) == False):
        i += 1
        print(f"{i}/{url_count}   {output_pathname}")
        download_image2(li)
    except:
      print(f'Error processing image url: {li}')
##############################################################################################################

##############################################################################################################
#https://www.pornhub.com/view_video.php?viewkey=ph619140ef20560
def get_pornhub_video_urls(url):
  videourls = []
  print(f"getting video URLs --> {url}")
  # response = requests.get(url)
  # if response.status_code != 200:
  #     print(f"Failed to fetch the page (status_code {response.status_code})")
  #     return videourls
  # soup = BeautifulSoup(response.text, 'html.parser')
  # ulist = soup.find_all('video', {"id": "video-post"})
  # for el in ulist:
  #   try:
  #     #a = el.find("a", {"class": "landscape"})
  #     a = el.find('source')
  #     imgurl = a['src']
  #     print(f"{url}     {imgurl}")
  #     videourls.append(imgurl)
  #   except:
  #     print(f'Error getting video from url: {url}')
  return videourls

def process_pornhub_page_urls(_urls, include_video = False):
  try:
      # filename = prefix + li.split('/')[-1]
      output_path = join(output_dir, "vids", "ph")
      #output_pathname = join(output_path, filename)
      # if (os.path.exists(output_pathname) == False):
      i = 0
      url_count = 1
      print(f"{i+1}/{url_count}   {output_path}   {_urls[i]}")
      #print(os.popen(f"cd {output_dir}"))
      output = os.popen(f'cd {output_path} && yt2 "{_urls[i]}"')
      print(output.read())
      print(output.close())
  except:
      print(f'Error processing page url: {li}')
##############################################################################################################

##############################################################################################################
#https://thefappening.pro/briana-agno-nude-the-fappening-129-photos/
def get_thefappeningpro_image_urls(url):
  imgurls = []
  print(f"getting image URLs --> {url}")
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return imgurls
  soup = BeautifulSoup(response.text, 'html.parser')
  ulist = soup.find_all('div', {"class": "entry-content"})
  for el in ulist:
    try:
      #a = el.find("a", {"class": "landscape"})
      #alist = el.find_all('img', {"class": "aligncenter size-medium"})
      # Find elements with a specific class
      # alist = el.select('.size-medium')
      # for el2 in alist:
      #   imgurl = el2['src']  #f"https://www.hotgirl.world{a['href']}"
      #   print(f"{url}     {imgurl}")
      #   imgurls.append(imgurl)
      alist = el.find_all('a')
      for el3 in alist:
        imgurl = el3['href']
        if (imgurl.startswith('https://thefappening.pro/wp-content') or imgurl.startswith('https://thefappening.pro/cnt')) and imgurl.endswith('.jpg'):
          print(f"{url}     {imgurl}")
          imgurls.append(imgurl)
      plist = el.find_all('p')
      for el2 in plist:
        alist = el2.find_all('a')
        for el3 in alist:
          imgurl = el3['href']
          if (imgurl.startswith('https://thefappening.pro/wp-content') or imgurl.startswith('https://thefappening.pro/cnt')) and imgurl.endswith('.jpg'):
            print(f"{url}     {imgurl}")
            imgurls.append(imgurl)
        ilist = el2.find_all('img')
        for el3 in ilist:
          imgurl = el3['src']
          if (imgurl.startswith('https://thefappening.pro/wp-content') or imgurl.startswith('https://thefappening.pro/cnt')) and imgurl.endswith('.jpg'):
            print(f"{url}     {imgurl}")
            imgurls.append(imgurl)
    except:
      print(f'Error getting image from url: {url}')
  return imgurls

def get_thefappeningpro_video_urls(url):
  videourls = []
  print(f"getting video URLs --> {url}")
  # response = requests.get(url)
  # if response.status_code != 200:
  #     print(f"Failed to fetch the page (status_code {response.status_code})")
  #     return videourls
  # soup = BeautifulSoup(response.text, 'html.parser')
  # ulist = soup.find_all('video', {"id": "video-post"})
  # for el in ulist:
  #   try:
  #     #a = el.find("a", {"class": "landscape"})
  #     a = el.find('source')
  #     imgurl = a['src']
  #     print(f"{url}     {imgurl}")
  #     videourls.append(imgurl)
  #   except:
  #     print(f'Error getting video from url: {url}')
  return videourls

def process_thefappeningpro_page_urls(_urls, include_video = False):
  _image_urls = []
  i = 0
  for url in _urls:
    i += 1
    print(f"========== {i} / {len(_urls)} ==========")
    imgurls = get_thefappeningpro_image_urls(url)
    videourls = get_thefappeningpro_video_urls(url) if include_video else []
    _image_urls.extend(imgurls)
    _image_urls.extend(videourls)
  _image_urls = remove_list_duplicates(_image_urls)
  url_count = len(_image_urls)
  print(f"\n  --- {url_count} DISTINCT IMAGE/VIDEO URLS ---\n")
  prefix = ""
  i = 0
  for li in _image_urls:
    try:
      filename = prefix + li.split('/')[-1]
      output_pathname = join(output_dir, filename)
      if (os.path.exists(output_pathname) == False):
        i += 1
        print(f"{i}/{url_count}   {output_pathname}")
        download_image2(li)
    except:
      print(f'Error processing image url: {li}')
##############################################################################################################

##############################################################################################################
def process_smutty_page(smutty_urls):
  smutty_image_urls = []
  i = 0
  for url in smutty_urls:
     i += 1
     print(f"========== {i} / {len(smutty_urls)} ==========")
     imgurls = get_image_urls_from_smutty_page(url)
     smutty_image_urls.extend(imgurls)
  smutty_image_urls = remove_list_duplicates(smutty_image_urls)
  print(f"\n{len(smutty_image_urls)} distinct image URLs\n")
  #
  prefix = ""
  i = 0
  for li in smutty_image_urls:
    try:
      filename = prefix + li.split('/')[-1]
      output_pathname = join(output_dir, filename)
      if (os.path.exists(output_pathname) == False):
        i += 1
        print(f"{i}   {output_pathname}")
        download_image(li)
    except:
      print(f'Error processing image url: {li}')

def deep_process_smutty_page(url):
   # "https://smutty.com/s/1VsU0/"
  smutty_urls = []
  smutty_urls1 = get_urls_from_smutty_page(url)
  i = 0
  for su in smutty_urls1:
     i += 1
     print(f"========== {i} / {len(smutty_urls1)} ==========")
     smutty_urls2 = get_urls_from_smutty_page(su)
     smutty_urls.extend(smutty_urls2)
     smutty_urls = remove_list_duplicates(smutty_urls)
  print("\n\n")
  #
  smutty_image_urls = []
  i = 0
  for url in smutty_urls:
     i += 1
     print(f"========== {i} / {len(smutty_urls)} ==========")
     imgurls = get_image_urls_from_smutty_page(url)
     smutty_image_urls.extend(imgurls)
  smutty_image_urls = remove_list_duplicates(smutty_image_urls)
  print(f"\n{len(smutty_image_urls)} distinct image URLs\n")
  #
  prefix = ""
  i = 0
  for li in smutty_image_urls:
    filename = prefix + li.split('/')[-1]
    output_pathname = join(output_dir, filename)
    if (os.path.exists(output_pathname) == False):
      i += 1
      print(f"{i}   {output_pathname}")
      download_image(li)
##############################################################################################################




##############################################################################################################
##############################################################################################################
#one URL only (no page #'s to process)
def get_generic_page_urls(_url):
  return [_url]

def deep_process_template_page(_url, fn1, fn2):
  #deep_urls = get_hotgirlworld_page_urls(_url, 1, 20)   # TODO: change 1,20 to start,end page #'s
  deep_urls = fn1(_url)
  if len(deep_urls) > 0:
     fn2(deep_urls)
  else:
     print(f"No page URLs to process from {_url}")
##############################################################################################################
##############################################################################################################




def thread_clipboard(name):
  clip = ""
  logging.info("Thread %s : starting", name)
  while (True):
    print("\n............................................................................................................")
    print("............................................................................................................")
    print("............................................................................................................")
    print("Waiting for copy URL to clipboard...")
    print()
    clipboard = pyperclip.waitForNewPaste()
    clip += clipboard + '\n'
    print(f"CLIPBOARD ==> {clipboard}")
    print("............................................................................................................")
    print("............................................................................................................")
    print("............................................................................................................\n")
    
    x = threading.Thread(target=thread_process, args=(clip.strip(), "PROCESS",))
    x.start()
    #x.join()
    clip = ""

    # clip_lines = clip.split('\n')   #clip.splitlines(clip)
    # print(f'\n\n\n===== {len(clip_lines)} LINES PASTED =====')
    # for li in clip_lines:
    #   lil = li.lower()
    #   if li.startswith('https://smutty.com/s/'):
    #     process_smutty_page([li])
    #   elif li.startswith('https://www.hotgirl.world'):
    #     deep_process_template_page(li, get_hotgirlworld_page_urls, process_hotgirlworld_page_urls)
    #   elif li.startswith('https://www.pornpics.com/galleries'):
    #     deep_process_template_page(li, get_generic_page_urls, process_pornpics_page_urls)
    #   else:
    #     print(f'\nUnknown site URL: {li}\n')
    # print('\n----- DONE PROCESSING -----\n')
    # time.sleep(2)
  logging.info("Thread %s: finishing", name)

def thread_process(clip, name):
  logging.info("Thread %s : starting", name)
  print("\n\n............................................................................................................")
  #print("............................................................................................................")
  print(f"  Processing clipboard ==> {clip}")
  clip_lines = clip.split('\n')   #clip.splitlines(clip)
  print(f'\n  --- {len(clip_lines)} LINES FROM CLIPBOARD ---')
  #print("............................................................................................................")
  print("............................................................................................................\n")
  for li in clip_lines:
    lil = li.lower()
    if lil.startswith('https://smutty.com/s/'):
      process_smutty_page([li])
    elif lil.startswith('https://www.hotgirl.world'):
      deep_process_template_page(li, get_hotgirlworld_page_urls, process_hotgirlworld_page_urls)
    elif lil.startswith('https://www.pornpics.com/galleries'):
      deep_process_template_page(li, get_generic_page_urls, process_pornpics_page_urls)
    elif lil.startswith('https://scandalplanet.com'):
      deep_process_template_page(li, get_generic_page_urls, process_scandalplanet_page_urls)
    elif lil.startswith('https://thefappeningblog.com/category/'):
      deep_process_template_page(li, get_thefappeningblog_page_urls, process_thefappeningblog_page_urls)
    elif lil.startswith('https://thefappeningblog.com/tag/'):
      deep_process_template_page(li, get_thefappeningblog_page_urls, process_thefappeningblog_page_urls)
    elif lil.startswith('https://thefappeningblog.com'):
      deep_process_template_page(li, get_generic_page_urls, process_thefappeningblog_page_urls)
    elif lil.startswith('https://thefappening.pro'):
      deep_process_template_page(li, get_generic_page_urls, process_thefappeningpro_page_urls)
    elif lil.startswith('https://www.pornhub.com'):
      deep_process_template_page(li, get_generic_page_urls, process_pornhub_page_urls)
    else:
      print(f'\nUnknown site URL: {li}\n')
  print('\n----- DONE PROCESSING -----\n')
  # time.sleep(2)
  logging.info("Thread %s: finishing", name)



############################################################ PIPELINE CLASS ################################################################
class Pipeline(queue.Queue):
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    def __init__(self):
        super().__init__(maxsize=200)
        # self.message = 0
        # self.producer_lock = threading.Lock()
        # self.consumer_lock = threading.Lock()
        # self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s:about to get from queue", name)
        value = self.get()
        logging.debug("%s:got %d from queue", name, value)
        return value
        # logging.debug("%s:about to acquire getlock", name)
        # self.consumer_lock.acquire()
        # logging.debug("%s:have getlock", name)
        # message = self.message
        # logging.debug("%s:about to release setlock", name)
        # self.producer_lock.release()
        # logging.debug("%s:setlock released", name)
        # return message

    def set_message(self, value, name):
        logging.debug("%s:about to add %d to queue", name, value)
        self.put(value)
        logging.debug("%s:added %d to queue", name, value)
        # logging.debug("%s:about to acquire setlock", name)
        # self.producer_lock.acquire()
        # logging.debug("%s:have setlock", name)
        # self.message = message
        # logging.debug("%s:about to release getlock", name)
        # self.consumer_lock.release()
        # logging.debug("%s:getlock released", name)
############################################################################################################################################

############################################################ PRODUCER AND CONSUMER #########################################################
SENTINEL = object()

# def producer(pipeline):
#     """Pretend we're getting a message from the network."""
#     for index in range(10):
#         message = random.randint(1, 101)
#         logging.info("Producer got message: %s", message)
#         pipeline.set_message(message, "Producer")
#     # Send a sentinel message to tell consumer we're done
#     pipeline.set_message(SENTINEL, "Producer")

# def consumer(pipeline):
#     """Pretend we're saving a number in the database."""
#     message = 0
#     while message is not SENTINEL:
#         message = pipeline.get_message("Consumer")
#         if message is not SENTINEL:
#             logging.info("Consumer storing message: %s", message)

def producer(pipeline, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")
    logging.info("Producer received EXIT event. Exiting")

def consumer(pipeline, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            "Consumer storing message: %s  (queue size=%s)",
            message,
            pipeline.qsize(),
        )
    logging.info("Consumer received EXIT event. Exiting")
############################################################################################################################################




#===========================================================================================================================================
#=========================================================== MAIN STARTS HERE ==============================================================
#===========================================================================================================================================
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    
    # pipeline = Pipeline()
    # event = threading.Event()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     executor.submit(producer, pipeline, event)
    #     executor.submit(consumer, pipeline, event)
    #     #executor.submit(thread_clipboard, args=("CLIPBOARD",))
    #     #executor.submit(thread_process, args=("PROCESS  ",))
    #     time.sleep(3.0)
    #     logging.info("Main: about to set event")
    #     event.set()

    logging.info("Main             : before creating thread")
    x = threading.Thread(target=thread_clipboard, args=("CLIPBOARD",))
    logging.info("Main             : before running thread")
    x.start()
    logging.info("Main             : wait for the thread to finish")
    x.join()
    logging.info("Main             : all done")

    sys.exit()
#===========================================================================================================================================
#===========================================================================================================================================
#===========================================================================================================================================

 

# <a href="/G02DE763/1AE42A2" class="img-container" target="_self">
#     <img src="/images/plc.gif" class="tr-placeholder"/>
#     <img class="static" src="https://cdn5-thumbs.motherlessmedia.com/thumbs/1AE42A2.jpg" data-strip-src="https://cdn5-thumbs.motherlessmedia.com/thumbs/1AE42A2.jpg" alt="Unsorted Sexiness 33"/>
# </a>
# <div class="captions">
#     <a href="/G02DE763/1AE42A2" title="Unsorted Sexiness 33" class="caption title pop plain">Unsorted Sexiness 33</a>

#process_big_image_page("https://motherless.com/GI3247CE8?page=2")
#process_big_image_pages("https://motherless.com/GI02DE763")

#process_image__pages("https://motherless.com/GI02DE763")
#process_image_pages("https://motherless.com/GI3247CE8")
#process_image__pages("https://motherless.com/GI10D4940")

#process_video__pages("https://motherless.com/GV02DE763")
#process_video__pages("https://motherless.com/GV3247CE8")
#process_video__pages("https://motherless.com/GV10D4940")

#download_image("https://cdn5-thumbs.motherlessmedia.com/thumbs/80DB975.jpg", False)

sys.exit()



tags = get_tags("http://www.babeimpact.com/galleries/mia-rosing-00.html", 'img')
for t in tags:
    if "Mia" in t.__repr__():
        print(t)
sys.exit()

images = get_images("http://www.nightdreambabe.com/natural-beauty-lily-xo")
for im in images:
    if im.size[0]>500 and im.size[1]>500:
        print(im.size)
print()

images = get_images("http://www.8boobs.com/lighting-effect/")
for im in images:
    print(im.size)
print()



# If you want to check if page exists and don't want to download the whole page, you should use Head Request:
import httplib2
h = httplib2.Http()
resp = h.request("http://www.google.com", 'HEAD')
assert int(resp[0]['status']) < 400

# If you want to download the whole page, just make a normal request and check the status code. Example using requests:
import requests
response = requests.get('http://google.com')
assert response.status_code < 400


#<div id="smutty_related" class="span-16 last">
#<div class="swidget_float">
#<a href="/s/8aUsw/" class="landscape">
#<img class="yesPopunder" src="//s.smutty.com/media_.....jpg" >
#</a>
#</div>


#smutty_urls = ["https://smutty.com/s/BiOJI/", "https://smutty.com/s/blS2Q/", "https://smutty.com/s/GJqoj/",
#               "https://smutty.com/s/xKAj0/", "https://smutty.com/s/IhBuI/", "https://smutty.com/s/iY87c/"]
#smutty_urls = ["https://smutty.com/s/sv1FC/", "https://smutty.com/s/OMMwb/", "https://smutty.com/s/xEPvy/",
#              "https://smutty.com/s/5lXAY/", "https://smutty.com/s/ncsy8/", "https://smutty.com/s/JN7bf/",
#              "https://smutty.com/s/MsQhU/", "https://smutty.com/s/GJqoj/", "https://smutty.com/s/4FdZt/",
#              "https://smutty.com/s/d0eQ4/"]
#https://smutty.com/s/75kY9/
#https://smutty.com/s/d6Z2T/
#https://smutty.com/s/ARExS/
#https://smutty.com/s/KuEpI/
#https://smutty.com/s/xxEdT/
#https://smutty.com/s/a8ChA/
#https://smutty.com/s/vKwQL/
#https://smutty.com/s/S0mKL/
#https://smutty.com/s/hq6ai/
#https://smutty.com/s/7lbrh/
#https://smutty.com/s/qlcQl/
#https://smutty.com/s/BALbl/
#https://smutty.com/s/NGdnf/
#https://smutty.com/s/uRmCV/
#https://smutty.com/s/Cnxng/
#https://smutty.com/s/TDMAF/
#https://smutty.com/s/Tyzv5/
#https://smutty.com/s/97NFv/
#https://smutty.com/s/ZiLLQ/
#https://smutty.com/s/LXLo1/
#https://smutty.com/s/FecKx/


#process_template_pages(['https://www.hotgirl.world/g/0mj1qwm5.html/?page=5'])
#deep_process_template_page('https://www.hotgirl.world/g/0mj1qwm5.html/?page=5')
#deep_process_template_page('https://www.hotgirl.world/g/x3egonm9.html/')
#deep_process_template_page('https://www.hotgirl.world/g/vm9l26m0.html')
