# libraries
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

# creating a class that will allow us to interact with the Twitter API
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis and tweeting.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'JiOetyA2MR50uaKJ6kgHqST7i'
        consumer_secret = 'XRHRlTObTPTpVq4RJg6keFQDYOcM9NF3dFiiYhAugyLKNlUqAQ'
        access_token = '1440487672863027204-7XqzjfxDwEVitNKpX6cf7nAU2CAZL3'
        access_token_secret = 'P7U7zaDQWPRwmeeKXQLPBBhqHW4Fxn4VcjsZJpwN7bI9h'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def tweet(self, message):
        '''
        Method to post a tweet with the given message.
        '''
        try:
            self.api.update_status(message)
            print("Tweet posted successfully!")
        except tweepy.TweepError as e:
            print(f"Error: {e}")

# Create an instance of the TwitterClient class
client = TwitterClient()

# Post a tweet
tweet_text = "Hello, World!"
client.tweet(tweet_text)

'''
DEAD CODE

# Search for tweets containing a specific keyword or hashtag
keyword = "bitcoin"
tweets = client.api.search_tweets(q=keyword, count=10)

# Print the tweets
for tweet in tweets:
    print(tweet.text)

'''
    """ DEAD CODE FROM THE CLASS - DEPRECATED ENDPOINTS THAT NO LONGER EXIST ON X
    
    # creating a method to get the tweets of a specific user
    def get_user_tweets(self, username, count=5):
        tweets = []
        try:
            for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=username).items(count):
                tweets.append(tweet.text)
        except tweepy.errors.Forbidden as e:
            print(f"Error: {e}")
        return tweets

    # creating a method to analyze the sentiment of the tweets
    def analyze_sentiment(self, tweets):
        sentiment_scores = []
        for tweet in tweets:
            analysis = TextBlob(tweet)
            sentiment_scores.append(analysis.sentiment.polarity)
        return sentiment_scores"""