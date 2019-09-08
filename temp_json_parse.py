import json, requests


########################### EXAMPLE 1 ##############################
url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

########################### EXAMPLE 2 ##############################
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

header = {'x-requested-with': 'XMLHttpRequest'}
#url = "https://www.daraz.pk/womens-kurtas-shalwar-kameez/?pathInfo=womens-kurtas-shalwar-kameez&page=2&YII_CSRF_TOKEN=31eb0a5d28f4dde909d3233b5a0c23bd03348f69&more_products=true"
url = "https://api.kraken.com/0/public/AssetPairs"
response = requests.get(url)    #, headers=header)
data = json.loads(response.text)
#print (data)
print "'data' has keys length %d:" % (len(data))
print data.keys()

########################### EXAMPLE 3 ##############################
json_data = '''
{
    "array": [
        1,
        2,
        3
    ],
    "boolean": true,
    "null": null,
    "number": 123,
    "object": {
        "a": "b",
        "c": "d",
        "e": "f"
    },
    "string": "Hello World"
}
'''

data = json.loads(json_data)

list_0 = [
    data['array'][0],
    data['array'][1],
    data['array'][2],
    data['boolean'],
    data['null'],
    data['number'],
    data['object']['a'],
    data['object']['c'],
    data['object']['e'],
    data['string']
]

print('''
array value 0           {0}
array value 1           {1}
array value 2           {2}
boolean value           {3}
null value              {4}
number value            {5}
object value a value    {6}
object value c value    {7}
object value e value    {8}
string value            {9}
'''.format(*list_0))


########################## MISC OTHER EXAMPLES ##############################

#header = {'x-requested-with': 'XMLHttpRequest'}
#url = "https://www.daraz.pk/womens-kurtas-shalwar-kameez/?pathInfo=womens-kurtas-shalwar-kameez&page=2&YII_CSRF_TOKEN=31eb0a5d28f4dde909d3233b5a0c23bd03348f69&more_products=true"
#url = "https://api.kraken.com/0/public/AssetPairs"
#url = "https://api.kraken.com/0/public/Ticker?pair=XXRPZUSD,XXRPXXBT"
url = "https://api.kraken.com/0/public/Ticker?pair=XBTCZEUR"
response = requests.get(url)    #, headers=header)
data = json.loads(response.text)
#print (data)
print "'data' has keys length %d:" % (len(data))
print data.keys()

sys.exit()

URL = "https://api.kraken.com/0/public/AssetPairs"
#URL = "https://api.kraken.com/0/public/Ticker?pair=XXRPZUSD,XXRPXXBT"
FILENAME_PAIR = "pair"+ ".json"
response = urllib.urlopen(URL)
pairinfo_dict = json.loads(response.read())
with open(FILENAME_PAIR, 'wb') as outfile:
    json.dump(pairinfo_dict, outfile)

sys.exit()
#quit()

