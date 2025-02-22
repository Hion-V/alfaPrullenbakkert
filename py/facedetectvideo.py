import cv2
import sys
import servo as hserv
#cascPath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

hastrig = False
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    facecount = 0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #++facecount
    #if (facecount == 1):
      #if (hastrig == False):
	hserv.open()
	hserv.close()
        #hastrig = True
    #elif (facecount == 0):
        #hastrig = False
    # Display the resulting frame
    #cv2.imshow('Video', frame)

    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
