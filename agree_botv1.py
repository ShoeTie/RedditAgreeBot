import praw 
import config
import time
from random import randint

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Shutei Agrees v0.1")
	return r

def run_bot(r):
	for comment in r.subreddit('all').stream.comments():
		if "I feel like" in comment.body:
			comment.reply(agree_synonyms[randint(0,size-1)])
			#print ("done!")
			print (comment.body)

			time.sleep(300)

agree_synonyms = ["I agree.", "Can't say I disagree.", "You've got a good point there.", "Hey, you're right!", "I concur", "The statement above is one I can get behind!", "I see where you're coming from."]
size = len(agree_synonyms)

r = bot_login()

while True:
	run_bot(r)