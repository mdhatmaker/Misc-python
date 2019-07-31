import tweepy
import time
from textblob import TextBlob


def process_friend(friend):
    return
    print(friend.screen_name)
    return

def process_status(status):
    return

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        text = status.text
        ascii_text = text.encode('ascii', 'ignore')
        print(text)
        blob = TextBlob(ascii_text)
        #print "sentiment [-1.0,1.0]: {0}    polarity [0.0,1.0]: {1}".format(blob.sentiment, blob.sentiment.polarity)
        sentiment = blob.sentiment
        print("polarity: {0:.2f}   subjectivity: {1:.2f}".format(sentiment.polarity, sentiment.subjectivity))
        print()
        return
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

        
################################################################################
"""
try:
    redirect_url = auth.get_authorization_url()
except:
    print "Error! Failed to get request token."
"""

"""
consumer_key = "00X4ZIFSBTf8f12nx2AA4g6nR"
consumer_secret = "e1wHQ4XORefZTRimnaRwnS900fsGSX9szAa7dGlQJmZlEBr3sK"
access_token = "1600231327-XO6kjWNJNdIIKP3RrETUQPqVGfoFt04SBu7uVI7"
access_token_secret = "BxamMNQhMgHksWFJvKaQCuZtVyCagWqMkLCWTUi2n8YNJ"
"""
consumer_key = "UDU1sgRZEcSvK011X6PEwDLpB"
consumer_secret = "LvlH9l7lNt9ZXISsWwfbZH7dlYzBjTrmyGQUdBF1d864Opei3k"
access_token = "1114249425927458816-cNbbxcxUj1nvXpnUgclZY3heA1SmTb"
access_token_secret = "ZHqScLrGxnBwXTmoFhjDups0p42s3rkehsrqDCgnzX2su"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#timeline_tweets = api.home_timeline()
#timeline_tweets = api.user_timeline('@TRHLofficial')
#timeline_tweets = api.user_timeline('@TRHLofficial', count=200, page=1)
#timeline_tweets = api.user_timeline('@TRHLofficial', max_id='1154940965318201344', count=200, page=1)
timeline_tweets = api.user_timeline('@TRHLofficial', max_id='1154238648130461698', count=200, page=1)
i = 0
for tweet in timeline_tweets:
    i += 1
    text = tweet.text.encode('utf-8')
    ascii_text = str(tweet.text.encode('ascii', 'ignore'))
    id = tweet.id_str
    #print(ascii_text[2:3]=='@')
    if (ascii_text[2:3]=='@' or ascii_text[2:4]=='RT'): #  text.startswith('@') or text.startswith('RT')):
        continue
    print("{0}: {1} {2}".format(i, id, text))
    """
    blob = TextBlob(ascii_text)
    #print "sentiment [-1.0,1.0]: {0}    polarity [0.0,1.0]: {1}".format(blob.sentiment, blob.sentiment.polarity)
    sentiment = blob.sentiment
    print("polarity: {0:.2f}   subjectivity: {1:.2f}".format(sentiment.polarity, sentiment.subjectivity))
    print()
    """
print()

# Get the User object for a specified username
#user = api.get_user('MaximusHead')
user = api.get_user('MichaelMercerXX')
print("screen name: {0}".format(user.screen_name))
print("# followers: {0}".format(user.followers_count))
#for friend in user.friends():
#   print friend.screen_name
print()

print("Creating stream listener...")
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# Most cases will use filter, the user_stream, or the sitestream
#myStream.filter(track=['aapl', 'goog'], async=False)




"""
# Iterate through all of the authenticated user's friends
for friend in limit_handled(tweepy.Cursor(api.friends).items()):
    # Process the friend here
    process_friend(friend)

# Iterate through the first 200 statuses in the friends timeline
for status in limit_handled(tweepy.Cursor(api.friends_timeline).items(200)):
    # Process the status here
    process_status(status)

for follower in limit_handled(tweepy.Cursor(api.followers).items()):
    if follower.friends_count < 300:
        print follower.screen_name
"""

