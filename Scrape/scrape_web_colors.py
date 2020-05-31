from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys

"""
This script takes a URL to a website containing a table with color information.

We will use BeautifulSoup to parse this website's HTML an a spcific table within.
"""

from f_chart import *
print(get_color('black'))
print(get_color('crimson'))
sys.exit()

# INPUTS:
# url: URL of website to scrape
# output_filename: resulting dataframe will be written to this .CSV file
url = "http://www.cloford.com/resources/colours/500col.htm"
output_filename = "web_colors.csv"


print("Requesting " + url + "...")
r = requests.get(url)
data = r.text
print("Creating BeautifulSoup parser...")
soup = BeautifulSoup(data, "html.parser")

# BeautifulSoup example of finding all links on a site
#for link in soup.find_all('a'):
#    print(link.get('href'))

print("Finding tables in web page...")
tables = soup.findChildren('table')
print("Found {0} tables.".format(len(tables)))

print("Iterating through tables to locate specific table...")
color_table = None
for i in range(0, len(tables)):
    t = tables[i]
    if t.has_attr('class') and 'webcol' in t['class']:
        color_table = t
        break

if color_table == None:
    print("Table not found.")
    sys.exit()
    
print("Found table.")

print("Finding rows in table...")
rows = color_table.findChildren(['th', 'tr'])
print("Found {0} rows.".format(len(rows)))

data_rows = []

print("Iterating through rows...")
for row in rows:
    cells = row.findChildren('td')
    #for cell in cells:
    #    value = cell.string
    #    print "[%s]" % value
    if len(cells) > 6:
        color_name = cells[0].string.strip()
        if '*' in color_name:
            if color_name.endswith('*'):
                color_name = color_name.strip('*')
                print(color_name)
            else:
                print(color_name)
                splits = color_name.split('(')
                splits2 = splits[1].split(')')
                #print splits[0], splits2[0]
                color_name = splits[0].strip()
        color_hex = cells[3].string
        color_r = cells[4].string
        color_g = cells[5].string
        color_b = cells[6].string
        li = [color_name, color_hex, color_r, color_g, color_b]
        data_rows.append(li)

df = pd.DataFrame(data_rows, columns=['Color_Name','Hex','R','G','B'])
df.to_csv(output_filename, index=False)

print()
print("Output to dataframe file:", "'{0}'".format(output_filename))
print()
