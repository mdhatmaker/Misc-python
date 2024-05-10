import sys
from PIL import Image
from os.path import join
import os
#import requests
#import re
from scrape_tools import *



def download_images_from_url_list(smutty_image_urls):
    prefix = ""
    i = 0
    for li in smutty_image_urls:
      filename = prefix + li.split('/')[-1]
      output_pathname = join(output_dir, filename)
      if (os.path.exists(output_pathname) == False):
        i += 1
        print(f"{i}   {output_pathname}")
        download_image(li)
    return

def get_image_urls_from_smutty_pages(smutty_urls):
    smutty_image_urls = []
    i = 0
    for url in smutty_urls:
       i += 1
       print(f"========== {i} / {len(smutty_urls)} ==========")
       imgurls = get_image_urls_from_smutty_page(url)
       smutty_image_urls.extend(imgurls)
    smutty_image_urls = remove_list_duplicates(smutty_image_urls)
    return


################################################################################################################
#smutty_url = 'https://smutty.com/s/Fp701/'
#smutty_url = 'https://smutty.com/s/4rUfR/'
#smutty_url = 'https://smutty.com/s/MxqJA/'
#smutty_url = 'https://smutty.com/s/uka74/'
#smutty_url = ''https://smutty.com/s/OdO4n/'

urls = ['https://smutty.com/s/VEYDI/', 'https://smutty.com/s/TJQkm/',
        'https://smutty.com/s/etBIR/', 'https://smutty.com/s/IBRlv/', 'https://smutty.com/s/EIBEl/', 'https://smutty.com/s/Q3wcZ/',
        'https://smutty.com/s/1SMQ3/', 'https://smutty.com/s/fnQSZ/', 'https://smutty.com/s/gCqQy/', 'https://smutty.com/s/nGnOm/' ]

for smutty_url in urls:
    image_urls = get_image_urls_from_smutty_page(smutty_url)
    download_images_from_url_list(image_urls)


print("\nDone.")
sys.exit()
