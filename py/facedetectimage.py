import cv2
import sys
import os
import servo
import ultra as ultra

open = False
avgfaces = []
while(True):
	if(ultra.getDist() < 5):
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
		if (len(avgfaces) >= 5):
			avgfaces.pop(0)
		avgfaces.append(numfaces)
		totalnum = 0
		for (anum) in avgfaces:
			totalnum += anum 
		if (totalnum >2):
			if(open == False):
				print("More than 2 of the last 5 pictures had a face, OPEN!")
				open = True
				servo.open()
		if (totalnum <2):
			if(open == True):
				print("less than 2 of the last 5 pictures had a face, CLOSE!")
				open = False
				servo.halfClose()
				servo.close()
		#cv2.imshow("Faces found", image)
		cv2.waitKey(0)
	#else:
		#servo.close();
