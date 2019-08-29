import sys
import requests
import json

# https://developers.zomato.com/documentation

zipcodes = {}
with open("data/ZipCodes2LatLng.txt", "r") as filestream:
    for line in filestream:
        currentline = line.split(',')
        zipcodes[currentline[0]] = (currentline[1].strip(), currentline[2].strip())

keys = zipcodes.keys()
print(zipcodes['46383'])
print(zipcodes['60601'])



headers = {
    'Accept': 'application/json',
    'user-key': '228f0da1e4a4b932caf65799c855275d',
}

params = (
    ('count', '20'),
    ('lat', '41.8859752'),
    ('lon', '-87.6336453'),
    ('radius', '1600'),
)

response = requests.get('https://developers.zomato.com/api/v2.1/search', headers=headers, params=params)

print('\n\n\n')
#print(response.content)

j = json.loads(response.content)    #'{"one" : "1", "two" : "2", "three" : "3"}')
#['results_found', 'results_start', 'results_shown', 'restaurants']
print(j['results_found'], j['results_start'], j['results_shown'])
rs = j['restaurants']

"""
dict_keys(['R', 'apikey', 'id', 'name', 'url', 'location',
    'switch_to_order_menu', 'cuisines', 'timings', 'average_cost_for_two',
    'price_range', 'currency', 'highlights', 'offers', 'opentable_support',
    'is_zomato_book_res', 'mezzo_provider', 'is_book_form_web_view',
    'book_form_web_view_url', 'book_again_url', 'thumb', 'user_rating',
    'all_reviews_count', 'photos_url', 'photo_count', 'photos', 'menu_url',
    'featured_image', 'has_online_delivery', 'is_delivering_now',
    'include_bogo_offers', 'deeplink', 'is_table_reservation_supported',
    'has_table_booking', 'events_url', 'phone_numbers', 'all_reviews',
    'establishment', 'establishment_types'])
"""
for i in range(len(rs)):
    r = rs[i]['restaurant']
    #print(r.keys())
    location = r['location']
    url = r['url']
    murl = r['menu_url']
    rid = r['id']
    print(i+1, rid, r['name'], location['address'], r['price_range'], r['average_cost_for_two'])  #r['R'])
    #print(murl)

    params = (
        ('res_id', rid),
    )
    #response = requests.get('https://developers.zomato.com/api/v2.1/dailymenu', headers=headers, params=params)
    #print(response.content)
    #j = json.loads(response.content)
    #print(j.keys())
