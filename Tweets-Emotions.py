import twitter
api = twitter.Api(consumer_key='MB1BUSegCKyzz0Zxf8QhaWpA5',
                  consumer_secret='7FeuVqyGFt6qCJs8IBo59jQI6P3khaK4jVmq13PzFJxzeda7Op',
                  access_token_key='1837672465-eRV1Fu2cDfyexzpRilSYCwT7Y11dWP3xSsM8T1o',
                  access_token_secret='rZnby1WIri9vtNnMwX1fUxmF8Zk2AQAob4aH5BGuxV4Iy')

print(api.VerifyCredentials())
print '/************ public status messages **************/'
statuses = api.GetUserTimeline(screen_name='maurosanchez93')
print([s.text for s in statuses])

print '/************ user"s friends **************/'
users = api.GetFriends()
print([u.name for u in users])

print '/************ Twitter status message **************/'
#status = api.PostUpdate('Me gusta python-twitter!')
#print(status.text)
'''
# Import the necessary package to process data in JSON format
try:
	import json
except ImportError:
	import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 'https://api.twitter.com/oauth/access_token'
ACCESS_SECRET = 'https://api.twitter.com/oauth/secret_token'
CONSUMER_KEY = 'MB1BUSegCKyzz0Zxf8QhaWpA5'
CONSUMER_SECRET = '7FeuVqyGFt6qCJs8IBo59jQI6P3khaK4jVmq13PzFJxzeda7Op'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
	tweet_count -= 1
	# Twitter Python Tool wraps the data returned by Twitter 
	# as a TwitterDictResponse object.
	# We convert it back to the JSON format to print/score
	print json.dumps(tweet)  
	
	# The command below will do pretty printing for JSON data, try it out
	# print json.dumps(tweet, indent=4)
	
	if tweet_count <= 0:
		break
'''
