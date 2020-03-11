from bs4 import BeautifulSoup
import requests
from difflib import SequenceMatcher
from os.path import basename, splitext
import sys
from datetime import datetime


def similar(a,b):
	return SequenceMatcher(None, a, b).ratio()
  
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
        print utext
        return

    text = utext.encode('ascii', 'xmlcharrefreplace')
    f.write(text + '\n')
    print ".",
    return
    
################################################################################

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
