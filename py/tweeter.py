#!/usr/bin/env python
import sys
from twython import Twython
import os

def tweet():
	#Set up api credentials
	apiKey = 'LBZ706xwM3fn64j6TQ5QVYdNP'
	apiSecret = 'qcs4nUhrjoHAPFaK8MhlJqGnajf9GJo0t5AeN4LvFINQKHfofZ'
	accessToken = '1089376871089954817-414StdLiHgugpvf5DMeHIOigB39DrF'
	accessTokenSecret = 'VK3yFVT5xHImlKkJbHW9IHten9EwyV53tJElIGA88pYAX'
	#Take a picture and load it into var "file"
	file = open('image.jpg', 'rb')
	#Connect to twitter api and verify credentials
	twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
	twitter.verify_credentials()
	#Upload the picture to twitter and then add it to a new tweet.
	response = twitter.upload_media(media=file)
	twitter.update_status(status='I threw away my garbage!', media_ids=[response['media_id']])
