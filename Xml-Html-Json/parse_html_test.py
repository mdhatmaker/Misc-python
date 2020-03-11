from lxml import html
import requests

#page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
page = requests.get('http://www.freesound.org/people/touchassembly/sounds/146321/')
tree = html.fromstring(page.text)

print tree

mp3 = tree.xpath("//html/body/table/tbody/tr[65]/td[2]/span/span[4]/text()")
print mp3

xx = tree.xpath('/html/body/table/tbody/tr[63]/td[2]/span/span[4]/text()')
print xx

for el in tree.body.itertext():
    sel = el
    i = sel.find("wav")
    if (i >=0 ): print el

