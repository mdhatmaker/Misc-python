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

