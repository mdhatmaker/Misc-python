import tweepy
# assuming twitter_authentication.py contains each of the 4 oauth elements (1 per line)
#from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def printTweepyMethods(tweet):
	print "tweet", dir(tweet)
	print "////////////////"
	print "tweet._api", dir(tweet._api)
	print "////////////////"
	print "tweet.text", dir(tweet.text)
	print "////////////////"
	print "tweet.entities", dir(tweet.entities)
	print "////////////////"
	print "tweet.author", dir(tweet.author)
	print "////////////////"
	print "tweet.user", dir(tweet.user)
	return

def printTweet(tweet):
	print "Name:", tweet.author.name.encode('utf8')
	print "Screen-name:", tweet.author.screen_name.encode('utf8')
	print "Tweet created:", tweet.created_at
	print "Tweet:", tweet.text.encode('utf8')
	print "Retweeted:", tweet.retweeted
	print "Favourited:", tweet.favorited
	print "Location:", tweet.user.location.encode('utf8')
	print "Time-zone:", tweet.user.time_zone
	print "Geo:", tweet.geo
	# hashtags can be retrieved from the entities dictionary
	print tweet.entities.get('hashtags')
	print "//////////////////"
	return
		
# startDate/endDate are strings in format 'yyyy-mm-dd'
def search1(searchText, startDate, endDate):
	for tweet in tweepy.Cursor(api.search, q=(searchText), since=startDate, until=endDate).items():
		printTweet(tweet)
	return
	
def mostRecent1000Mentions(query):
	#query = 'python'
	max_tweets = 1000
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
	return searched_tweets

# Update: in response to Andre Petre's comment about potential memory consumption issues with tweepy.Cursor,
# I'll include my original solution, replacing the single statement list comprehension used above to compute
# searched_tweets with the following:
def a_mostRecent1000Mentions(query):	
	searched_tweets = []
	last_id = -1
	while len(searched_tweets) < max_tweets:
	    count = max_tweets - len(searched_tweets)
	    try:
	        new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
	        if not new_tweets:
	            break
	        searched_tweets.extend(new_tweets)
	        last_id = new_tweets[-1].id
	    except tweepy.TweepError as e:
	        # depending on TweepError.code, one may want to retry or wait
	        # to keep things simple, we will give up on an error
	        break
	return searched_tweets

def search2(query, how_many):
	search_results = api.search(q=query, count=how_many)
	for i in search_results:
		printTweet(i)
	return
								
# ************* MAIN PROGRAM BEGINS HERE ****************
API_KEY = ckey = "KhbkyFAN3dhsi5sWzMZQbv1Rb"
API_SECRET = csecret = "2PInJh9McfKk4ubcCRmqF3TK2ybXJFWAsEDPdVz9IPCvQIaWwr"
ACCESS_TOKEN = atoken = "1600231327-lgVHMOiHfewpbixOzy0Ns99szxYYZXb6K7A03CK"
ACCESS_TOKEN_SECRET = asecret = "wCuVGEanPWuV3Zv6VDvMvdTizbs1ITCSrNnRZrX9HKthQ"

auth = tweepy.auth.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret, 'access_token_key':atoken, 'access_token_secret':asecret}
#auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
#api = tweepy.API(auth)

search2("kobe", 10)
#search1("kobe", "2015-07-15", "2015-07-22")
