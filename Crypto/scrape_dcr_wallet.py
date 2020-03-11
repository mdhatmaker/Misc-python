from bs4 import BeautifulSoup
import requests
from difflib import SequenceMatcher
from os.path import basename, splitext
import os
import sys
from datetime import datetime


MEGABYTE = 1048576
GIGABYTE = 1073741824

base_url = "https://1337x.to"


def similar(a,b):
	return SequenceMatcher(None, a, b).ratio()

def get_html(url):
    debug = {'verbose': sys.stderr}
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r  = requests.get(url, headers = user_agent)    #, config=debug)
    #print(r.status_code)
    print(r)
    html = r.text
    #print(html)
    return html

def get_soup(url):
    html = get_html(url)
    bs = BeautifulSoup(html, "html.parser")
    return bs

def get_stuff(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    #links = []
    next_link = None
    for link in soup.find_all('a'):
        if link.text.lower().strip() == 'next':
            next_link = link.get('href')
            #print(next_link)            
            #links.append(next_link)
            break
    div = soup.find('div', {'class':'inner-entry-content cf'})
    #print div.text
    # Or for find_all...
    #for res in div:
    #    print res.text
    return (div, next_link)

def output(utext, f=None):
    if f==None:
        print(utext)
        return
    text = utext.encode('ascii', 'xmlcharrefreplace')
    f.write(text + '\n')
    print(".", end='')
    return

def get_magnet_links(bs):
    li = []
    links = bs.findAll(lambda tag: tag.name=='a', href=True)
    for link in links:
        href = link['href']
        if href.startswith('magnet'):
            #print(i, href)
            li.append(link)
    return li

import sys , subprocess
def open_magnet(magnet):
    """Open magnet according to os."""
    if sys.platform.startswith('linux'):
        subprocess.Popen(['xdg-open', magnet], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif sys.platform.startswith('win32'):
        os.startfile(magnet)
    elif sys.platform.startswith('cygwin'):
        os.startfile(magnet)
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(['open', magnet], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        subprocess.Popen(['xdg-open', magnet], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def open_magnet_link(link):
    magnet_link = link['href']
    #print(magnet_link)
    open_magnet(magnet_link)
    return

def open_1337x_magnet(url):
    #url = 'https://1337x.to/torrent/3236676/Elementary-S06E21-HDTV-x264-KILLERS-eztv/'
    bs = get_soup(url)
    links = get_magnet_links(bs)
    open_magnet_link(links[0])
    return

def get_search_results(bs):
    # returns list - each list item is list of <td> columns
    # 0=name 1=se 2=le 3=time 4=size 5=uploader
    tables = bs.find_all('table')
    #for x in tables:
    #    print(x.name)
    #table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="Table1") 
    table = tables[0]
    rows = table.findAll(lambda tag: tag.name=='tr')
    li = []
    for row in rows[1:]:    # skip the first row which has the column headers
        #print(row)
        #col_text = row.text.split()
        #print(col_text[0])
        cols = row.findAll(lambda tag: tag.name=='td')
        li.append(cols)
    return li

def byte_size(strSize):
    #strSize = "205.4 MB"
    size = None
    if strSize.endswith('MB'):
        size = float(strSize[:-3]) * MEGABYTE
    elif strSize.endswith('GB'):
        size = float(strSize[:-3]) * GIGABYTE
    else:
        print('ERROR')
    return size

def get_search_row_size(cols):
    text = cols[4].text
    i = text.find(' ')
    strSize = text[:i+3]
    return byte_size(strSize), strSize

def get_search_row_link(cols):
    col = cols[0]
    links = col.findAll(lambda tag: tag.name=='a', href=True)
    link = links[1]
    link_url = base_url + link['href']
    return link_url

def get_search_url(search_for, page=1):
    #search_for = "elementary s06"
    search = search_for.replace(' ', '+')
    search_url = "{}/search/{}/{}/".format(base_url, search, page)
    print(search_url)
    return search_url

################################################################################

print('======================================================================================')

#url = "https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/navigation/tabbed-page"
#soup = get_soup(url)

with open('./data/test.html', 'r') as content_file:
    html = content_file.read()
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all('wallet'):
    for x in link.find_all('coin'):
        print(x.name, x['symbol'], x.text)

sys.exit()

