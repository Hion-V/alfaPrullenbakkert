#!/usr/bin/env python
import sys
from twython import Twython
import os
#Set up api credentials
apiKey = '2CzFUz72dezAIBXXXdRoVkIi3'
apiSecret = 's6mxgPgMEUcfbTBDCmHCugunBH2mrGkiVSY22eL9JuQXZcpmqL'
accessToken = '4728772521-455yCUGrPEFi5onbP8KlsBxcIuu9DKrejgVz1LH'
accessTokenSecret = 'iJWlUwZVtqF1WXw4A0rm0nQ1oMFFhZdfFyJXmGylrGTBw'
#Take a picture and load it into var "file"
os.system("fswebcam images/lol.jpg")
file = open('images/lol.jpg', 'rb')
#Connect to twitter api and verify credentials
twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
twitter.verify_credentials()
#Upload the picture to twitter and then add it to a new tweet.
response = twitter.upload_media(media=file)
twitter.update_status(status='I threw away my garbage!', media_ids=[response['media_id']])