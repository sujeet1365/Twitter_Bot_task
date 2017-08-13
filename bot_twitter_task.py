#Used for read and write
#Fetched from https://apps.twitter.com/app

from sujeet_keys import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy, time, sys


#Used for read and write
#Fetched from https://apps.twitter.com/app by generating the access token

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def getTimeline(api, user):
    """
    this method gets the last 100 tweets from the user's timeline. This returns
    a list of tweet objects, check Twitter's docs to learn more about them.
    """
    tweets = api.user_timeline(user.screen_name, count=100)
    tweets = [tweet for tweet in tweets]
    # this will print out the FULL contents of the first tweet object in the
    # list. This is useful to see the data fields available to use for other
    # methods you may want to make.
    print(tweets[0])
    return tweets

## To print the followers of a particular user in Twitter
#Code snippet taken from http://docs.tweepy.org/en/v3.5.0/code_snippet.html
print '\nFollowers in Twitter\n'
for number_of_user in tweepy.Cursor(api.followers, screen_name="krish020993").items():
    print number_of_user.screen_name

## To print names of people whom I am following
#Code snippet taken from http://docs.tweepy.org/en/v3.5.0/code_snippet.html
print '\nFollowing in Twitter\n'
for friend in tweepy.Cursor(api.friends).items():
	print friend.screen_name
