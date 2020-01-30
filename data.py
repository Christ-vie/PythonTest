from __future__ import print_function
import tweepy
import json

from pymongo import MongoClient

MONGO_HOST= 'mongodb://localhost/twitterdb'  
 
WORDS = ['je suis connecté']
 
CONSUMER_KEY = "0sVMx0oLDkFPqMxGEZkQQwj6i"
CONSUMER_SECRET = "U0XOkFy1Q9Q3sEXNq33BPF0cScrTxxtbGREtFq9lxnJFKlKjaX"
ACCESS_TOKEN = "1052923426728501250-ahd6yv26PyIDLynLHzpX69PJuATCZA"
ACCESS_TOKEN_SECRET = "hNds2hfkvidNJp1yrsrn17h13gjlQk6C8cFVEgnxb7w3i"


 
class StreamListener(tweepy.StreamListener):    
 
 
    def on_connect(self):
      
        print(" the streaming API")
 
    def on_error(self, status_code):
        
        print('il y a error : ' + repr(status_code))
        return False
 
    def on_data(self, data):
   
        try:
            client = MongoClient(MONGO_HOST)
            
            
            db = client.twitterdb
    
            
            datajson = json.loads(data)
            
            
            created_at = datajson['created_at']
 
            
            print("Tweet collecté à " + str(created_at))
            
            
            db.twitter_search.insert(datajson)
        except Exception as e:
           print(e)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
 

