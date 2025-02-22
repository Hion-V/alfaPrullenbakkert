import cv2
import sys
import os
import servo
import ultra as ultra
import time as time
import tweeter as twit
open = False
avgfaces = []
while(True):
	dist = ultra.getDist()
	if(dist < 15):
		os.system("fswebcam -q image.jpg");
		# Get user supplied values
		imagePath = "image.jpg"
		cascPath = "haarcascade_frontalface_default.xml"
		
		# Create the haar cascade
		faceCascade = cv2.CascadeClassifier(cascPath)
		
		# Read the image
		image = cv2.imread(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
		    gray,
		    scaleFactor=1.1,
		    minNeighbors=5,
		    minSize=(30, 30)
		    #flags = cv2.CV_HAAR_SCALE_IMAGE
		)
		
		print("Found {0} faces!".format(len(faces)))
		
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
		    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
		numfaces = len(faces)
		if (numfaces >0):
			#if(open == False):
				print("You have a face, OPEN!")
				open = True
				os.system("aplay Hello.wav");
				servo.open()
				while(ultra.getDist() < 10):
					print("waiting for hand removal");
					time.sleep(1);
				os.system("aplay bye.wav");
				servo.close();
				twit.tweet();
				
				
		#cv2.imshow("Faces found", image)
		cv2.waitKey(0)
	#else:
		#servo.close();
