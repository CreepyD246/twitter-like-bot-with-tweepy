# Importing Tweepy and time
import tweepy
import time

# Credentials (INSERT YOUR CREDENTIALS BELOW)
api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        #Liking the tweet
        try:
            client.like(tweet.id)
            print(tweet.text)

        except Exception as error:
            print(error)
        
        # delay between tweets
        time.sleep(1)

# Creating Stream object
stream = MyStream(bearer_token=bearer_token)

# Adding terms to search rules
stream.add_rules(tweepy.StreamRule("(#Python OR #programming) (-is:retweet -is:reply)"))

# Starting stream
stream.filter()
