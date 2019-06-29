import json, urllib, urllib2

GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
PLACES_BASE_URL = 'https://maps.googleapis.com/maps/api/place/search/json'
LOCAL_BASE_URL = 'http://ajax.googleapis.com/ajax/services/search/local'

def geocode(address, sensor, **geo_args):
    geo_args.update({
        'address': address,
        'sensor': sensor
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    results = json.load(urllib.urlopen(url))
    return results

def places(apikey, location, radius, sensor, **places_args):
    places_args.update({
        'key': apikey,
        'location': str(location['lat']) + ',' + str(location['lng']),
        'radius': radius,
        'sensor': sensor
    })

    url = PLACES_BASE_URL + '?' + urllib.urlencode(places_args)
    #print "URL: %s" % url
    #url = "https://maps.googleapis.com/maps/api/place/search/json?location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&sensor=false&key=AIzaSyAMnDVWP5s-yHEAu3aCimIGGsa3b98hINQ"
    results = json.load(urllib.urlopen(url))
    return results

def localSearch(q, v, **local_args):
    local_args.update({
        'q': q,
        'v': v
    })
    
    url = ('http://ajax.googleapis.com/ajax/services/search/local?' +
       'v=1.0&q=barack%20obama&key=AIzaSyAMnDVWP5s-yHEAu3aCimIGGsa3b98hINQ&userip=50.104.67.89')

    url = LOCAL_BASE_URL + '?' + urllib.urlencode(local_args)
    
    request = urllib2.Request(url, None, {'Referer': 'http://www.pacificderivatives.com'})
    response = urllib2.urlopen(request)
    
    results = json.load(response)
    return results


    
if __name__ == '__main__':
    googleAPIKey = 'AIzaSyAMnDVWP5s-yHEAu3aCimIGGsa3b98hINQ'
    loc = { "lat": -33.8722580, "lng": 151.1986550}
    #loc = "-33.8722580,151.1986550"
    
    geo_results = geocode(address="Chicago",sensor="false")    
    print json.dumps([s['formatted_address'] for s in geo_results['results']], indent=2)
    print
    
    places_results = places(apikey=googleAPIKey, location=loc, radius=500, sensor="false", types="food", name="harbour")
    print json.dumps([s['name'] for s in places_results['results']], indent=2)
    #print places_results['results']
    #print places_results
    print

    query = "Kumon"
    local_results = localSearch(q=query,v=1.0,key=googleAPIKey,userip="50.104.67.89")
    #print json.dumps([s['url'] for s in local_results['results']], indent=2)
    #print local_results
    #print local_results['responseData']['results']
    list = local_results['responseData']['results']
    for r in list:
        print r['titleNoFormatting']
        print r['url']
        print
    print
    
    
