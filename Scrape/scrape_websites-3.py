

from bs4 import BeautifulSoup
#import urllib2
import urllib.request as urllib2
#import requests
import sys
from PIL import Image
from os.path import join
import os
import requests
import re


output_dir = "/Users/michael/Downloads/scrape"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)



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
    
#download_image("https://cdn5-thumbs.motherlessmedia.com/thumbs/80DB975.jpg", False)


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
  response = requests.get(url)  #, headers=headers)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return
  soup = BeautifulSoup(response.text, 'html.parser')
  return get_smutty_image_from_soup(soup)

def get_smutty_image_from_soup(soup):
  image = soup.find("img", {"class": "yesPopunder image_perma_img inner_rounded"})
  if image is None:
     image = soup.find("img", {"class": "yesPopunder image_perma_img"})
  if image is None:
     image = soup.find("img", {"class": "yesPopunder"})
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
  print(f"getting URLs --> {url}")
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to fetch the page (status_code {response.status_code})")
      return imgurls
  soup = BeautifulSoup(response.text, 'html.parser')
  imgurl = get_smutty_image_from_soup(soup)
  imgurls.append(imgurl)
  swidgets = soup.find_all("div", {"class": "swidget_float"})
  for el in swidgets:
    a = el.find("a", {"class": "landscape"})
    href = f"https://smutty.com{a['href']}"
    imgurl = get_smutty_image_from_url(href)
    print(f"{href}     {imgurl}")
    imgurls.append(imgurl)
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


#smutty_urls = ["https://smutty.com/s/BiOJI/", "https://smutty.com/s/blS2Q/", "https://smutty.com/s/GJqoj/",
#               "https://smutty.com/s/xKAj0/", "https://smutty.com/s/IhBuI/", "https://smutty.com/s/iY87c/"]

#smutty_urls = ["https://smutty.com/s/sv1FC/", "https://smutty.com/s/OMMwb/", "https://smutty.com/s/xEPvy/",
#              "https://smutty.com/s/5lXAY/", "https://smutty.com/s/ncsy8/", "https://smutty.com/s/JN7bf/",
#              "https://smutty.com/s/MsQhU/", "https://smutty.com/s/GJqoj/", "https://smutty.com/s/4FdZt/",
#              "https://smutty.com/s/d0eQ4/"]


smutty_urls = []
smutty_urls1 = get_urls_from_smutty_page("https://smutty.com/s/ATN2I/")
i = 0
for su in smutty_urls1:
   i += 1
   print(f"========== {i} / {len(smutty_urls1)} ==========")
   smutty_urls2 = get_urls_from_smutty_page(su)
   smutty_urls.extend(smutty_urls2)
   smutty_urls = remove_list_duplicates(smutty_urls)

print("\n\n")

smutty_image_urls = []
i = 0
for url in smutty_urls:
   i += 1
   print(f"========== {i} / {len(smutty_urls)} ==========")
   imgurls = get_image_urls_from_smutty_page(url)
   smutty_image_urls.extend(imgurls)
smutty_image_urls = remove_list_duplicates(smutty_image_urls)

print(f"\n{len(smutty_image_urls)} distinct image URLs\n")

prefix = ""
i = 0
for li in smutty_image_urls:
  filename = prefix + li.split('/')[-1]
  output_pathname = join(output_dir, filename)
  if (os.path.exists(output_pathname) == False):
    i += 1
    print(f"{i}   {output_pathname}")
    download_image(li)


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

#process_big_image_page("https://motherless.com/GI3247CE8?page=2")
#process_big_image_pages("https://motherless.com/GI02DE763")

#process_image__pages("https://motherless.com/GI02DE763")
#process_image_pages("https://motherless.com/GI3247CE8")
#process_image__pages("https://motherless.com/GI10D4940")

#process_video__pages("https://motherless.com/GV02DE763")
#process_video__pages("https://motherless.com/GV3247CE8")
#process_video__pages("https://motherless.com/GV10D4940")

sys.exit()


# <a href="/G02DE763/1AE42A2" class="img-container" target="_self">
#     <img src="/images/plc.gif" class="tr-placeholder"/>
#     <img class="static" src="https://cdn5-thumbs.motherlessmedia.com/thumbs/1AE42A2.jpg" data-strip-src="https://cdn5-thumbs.motherlessmedia.com/thumbs/1AE42A2.jpg" alt="Unsorted Sexiness 33"/>
# </a>
# <div class="captions">
#     <a href="/G02DE763/1AE42A2" title="Unsorted Sexiness 33" class="caption title pop plain">Unsorted Sexiness 33</a>
    

tags = get_tags("http://www.babeimpact.com/galleries/mia-rosing-00.html", 'img')
for t in tags:
    if "Mia" in t.__repr__():
        print(t)
        
sys.exit()

images = get_images("http://www.nightdreambabe.com/natural-beauty-lily-xo")
for im in images:
    if im.size[0]>500 and im.size[1]>500:
        print(im.size)
        
print

images = get_images("http://www.8boobs.com/lighting-effect/")
for im in images:
    print(im.size)
    



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
