from bs4 import BeautifulSoup
import requests
from difflib import SequenceMatcher
from os.path import basename, splitext
import sys
from datetime import datetime


def similar(a,b):
	return SequenceMatcher(None, a, b).ratio()
  
def get_soup(url):
    r = requests.get(url)
    data = r.text
    print(r.status_code)
    print(r)
    soup = BeautifulSoup(data, "html.parser")
    return soup

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
    
################################################################################

base_url = "https://1337x.to"
search_for = "elementary s06"
search = search_for.replace(' ', '+')
page = 1
search_url = "{}/search/{}/{}/".format(base_url, search, page)

print('\n\n\n')
print(search_url)

url = search_url
debug = {'verbose': sys.stderr}
user_agent = {'User-agent': 'Mozilla/5.0'}
r  = requests.get(url, headers = user_agent)    #, config=debug)
#print(r.status_code)
print(r, end='\n\n')
html = r.text
#print(html)
bs = BeautifulSoup(html, "html.parser")
tables = bs.find_all('table')
#for x in tables:
#    print(x.name)
#table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="Table1") 
table = tables[0]
rows = table.findAll(lambda tag: tag.name=='tr')
for row in rows[1:]:    # skip the first row which has the column headers
    #print(row)
    col_text = row.text.split()
    print(col_text[0])
    cols = row.findAll(lambda tag: tag.name=='td')
    col = cols[0]
    links = col.findAll(lambda tag: tag.name=='a', href=True)
    link = links[1]
    link_url = base_url + link['href']
    print(link_url)
    continue
    i = 1
    for col in cols:
        #print(i, col)        
        if i == 1:
            links = col.findAll(lambda tag: tag.name=='a', href=True)
            #for link in links:
            #    print(link)
            link = links[1]
            link_url = base_url + link['href']
            print(link_url)
        i += 1
    print()

sys.exit()

soup = get_soup(search_url)

print(soup.text)

for link in soup.find_all('a'):
    print(link.text)

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