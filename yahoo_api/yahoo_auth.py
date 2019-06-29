import yql
from yql.storage import FileTokenStore
import os
import pprint
import json


#----------------------------------------------------------------------------------------------------------------
def query(q):
    return y3.execute(q, token=token).rows

def qprint(dict):
    print json.dumps(dict, indent=1)
    return

def nfl_player(player_id):
    query_string = 'select * from fantasysports.players where player_key="nfl.p.%s"' % player_id
    player_query = query(query_string)
    if len(player_query) > 0:
        return player_query[0]
    else:
        return {}

#----------------------------------------------------------------------------------------------------------------

consumer_key = 'dj0yJmk9bTJtUTNNbnJNdWdNJmQ9WVdrOVJYUk1WazFFTXpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD01Zg--'
consumer_secret = 'ddd0ff748e8f51bfff8f1bc31b1d55c2b2d15c01'

y3 = yql.ThreeLegged(consumer_key, consumer_secret)
_cache_dir = 'C:\\Projects\\MyProjects\\PYTHON\\yahoo_api'
if not os.access(_cache_dir, os.R_OK):
    os.mkdir(_cache_dir)
token_store = FileTokenStore(_cache_dir, secret='sasfasdfdasfdaf')

stored_token = token_store.get('foo')

if not stored_token:
    # Do the dance
    request_token, auth_url = y3.get_token_and_auth_url()
    print "Visit url %s and get a verifier string" % auth_url
    verifier = raw_input("Enter the code: ")
    token = y3.get_access_token(request_token, verifier)
    token_store.set('foo', token)
else:
    # Check access_token is within 1 hour-old and if not refresh it
    # and stash it
    token = y3.check_token(stored_token)
    if token != stored_token:
        token_store.set('foo', token)
        

#qry = 'select * from fantasysports.players where player_key="223.p.5479"'
#data_yql = y3.execute(qry, token=token)
#data = data_yql.rows

#"http://fantasysports.yahooapis.com/fantasy/v2/league/nfl/players;start=50"
#qry = 'select * from fantasysports.players where league_key="223"'
#data_yql = y3.execute(qry, token=token)
#data = data_yql.rows

#results = query('select * from fantasysports.players where player_key="nfl.p.5477"')
#pprint.pprint(results)
#print json.dumps(results, indent=1)

for id in range(5300, 5480):
    player = nfl_player(id)
    if player.has_key('name'):
        print "id:%s      " % id + player['name']['full']
    else:
        print "(%s)" % id

        
    
