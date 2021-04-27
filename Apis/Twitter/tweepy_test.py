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

consumer_key = "00X4ZIFSBTf8f12nx2AA4g6nR"
consumer_secret = "e1wHQ4XORefZTRimnaRwnS900fsGSX9szAa7dGlQJmZlEBr3sK"
access_token = "1600231327-XO6kjWNJNdIIKP3RrETUQPqVGfoFt04SBu7uVI7"
access_token_secret = "BxamMNQhMgHksWFJvKaQCuZtVyCagWqMkLCWTUi2n8YNJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
i = 0
for tweet in public_tweets:
    i += 1
    text = tweet.text.encode('utf-8')
    ascii_text = tweet.text.encode('ascii', 'ignore')
    print("{0}: {1}".format(i, text))
    blob = TextBlob(ascii_text)
    #print "sentiment [-1.0,1.0]: {0}    polarity [0.0,1.0]: {1}".format(blob.sentiment, blob.sentiment.polarity)
    sentiment = blob.sentiment
    print("polarity: {0:.2f}   subjectivity: {1:.2f}".format(sentiment.polarity, sentiment.subjectivity))
    print()
print()

# Get the User object for a specified username
user = api.get_user('MaximusHead')
print("screen name: {0}".format(user.screen_name))
print("# followers: {0}".format(user.followers_count))
#for friend in user.friends():
#   print friend.screen_name
print()

print("Creating stream listener...")
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# Most cases will use filter, the user_stream, or the sitestream
myStream.filter(track=['aapl', 'goog']) #, async=False)




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

