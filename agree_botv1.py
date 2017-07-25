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
		if "I feel like" in comment.body and comment.subreddit != ('SecondaryInfertility' or 'depression' or 'BipolarReddit' or'anxiety' or 'stopselfharm' or 'ADHD' or 'birthcontrol' or 'cripplingalcoholism' or 'suicidewatch' or 'ForeverAlone' or 'stopdrinking' or 'deadbedreooms' or 'SanctionedSuicide' or 'infertility' or 'seduction' or 'BreakUps' or 'nofap' or 'incels'):
			comment.reply(agree_synonyms[randint(0,size-1)])
			#print ("done!")
			print (comment.body)

			time.sleep(randint(5, 30))

agree_synonyms = ["I agree.", "Can't say I disagree.", "You've got a good point there.", "Hey, you're right!", "I concur.", "The statement above is one I can get behind!", "I see where you're coming from.", "You're absolutely correct!", "I can't disagree with that!", ]
size = len(agree_synonyms)

r = bot_login()

while True:
	run_bot(r)