from bs4 import BeautifulSoup
import urllib2
#import requests
import sys
from PIL import Image
from os.path import join


def download_image(url):
    fd = urllib2.urlopen(url)
    im = Image.open(fd)
    #print im.size
    return im

def get_tags(url, tag="img"):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    return soup.find_all(tag)

def get_images(url):
    img_tags = get_tags(url, 'img')
    imgs = []
    for img in img_tags:
        if img['src'].endswith(".jpg"):
            #print img
            try:
                im = download_image(img['src'])
                imgs.append(im)
            except:
                continue
    return imgs

def save_images(format_url, i1, i2, prefix=""):
    output_dir = "/Users/michael/Downloads"
    for i in range(i1, i2+1):
        url = format_url.format(i)
        #print url
        im = download_image(url)
        filename = prefix + url.split('/')[-1]
        #print im.size
        print filename
        im.save(join(output_dir, filename))
    return


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
    
sys.exit()

tags = get_tags("http://www.babeimpact.com/galleries/mia-rosing-00.html", 'img')
for t in tags:
    if "Mia" in t.__repr__():
        print t
        
sys.exit()

images = get_images("http://www.nightdreambabe.com/natural-beauty-lily-xo")
for im in images:
    if im.size[0]>500 and im.size[1]>500:
        print im.size
        
print

images = get_images("http://www.8boobs.com/lighting-effect/")
for im in images:
    print im.size
    
