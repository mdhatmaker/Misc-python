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

#open_1337x_magnet('https://1337x.to/torrent/3036321/Elementary-S06E06-HDTV-x264-LOL-eztv/')
#sys.exit()

#search_url = get_search_url("forged of blood", 1)
search_url = get_search_url("elementary s06", 2)
soup = get_soup(search_url)

li = get_search_results(soup)
print('\n', li[0][4].text, '\n')
print(get_search_row_size(li[0]))
print(get_search_row_link(li[0]))


sys.exit()

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



"""
(script_name, script_ext) = splitext(basename(__file__))

dt = datetime.now()
filename = script_name + " " + dt.strftime("%Y-%m-%d %H-%M-%S") + ".txt"
#print filename

f = open(filename, 'w')
#f = None

next_link = "http://www.trend-chaser.com/entertainment/23-movies-actors-hooking-up/?utm_source=tb&utm_medium=breitbartcom-tb&utm_term=10+Actors+Who+Actually+Did+It+On+Screen-https%3A%2F%2Fconsole.brax-cdn.com%2Fcreatives%2Fb86bbc0b-1fab-4ae3-9b34-fef78c1a7488%2FMSM_MAINSTREAM_MOVIES_632_oface_jennifer_msm_9a294115cf15e8623ca0ed9fdfae0991.600x500.png&utm_content=47712827&utm_campaign=659898-tb&utm_taboola_id=659898#D6cTC&D6cTCHN"

last_link = None
(div, next_link) = get_stuff(next_link)
while next_link != None:
    if last_link != None:
        sim = similar(last_link, next_link)
        #print sim
        if sim < 0.90: break
    #find_img = div.find('img')
    #if find_img != None:
    #    img = div.find('img').get('src')
    #    output("[{0}]".format(img), f)
    img = div.find('img').get('src')
    output("[{0}]".format(img), f)
    output(div.text + '\n', f)
    output("[{0}]".format(next_link), f)
    output("-" * 80, f)

    last_link = next_link
    (div, next_link) = get_stuff(next_link)
    
if f: f.close()

print
print "Output to file: '{0}'".format(filename)
"""