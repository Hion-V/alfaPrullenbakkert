import cv2
import sys
import os

cascPath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath);
#cascPath = sys.argv[1];

video_capture = cv2.VideoCapture(0);
lastfaces = 0;
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read();

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    );
    facecount = len(faces)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2);

    if (facecount > lastfaces):
        print("smerige kkrjunk");
        os.system("start mpg123 " + "file.mp3");
    

    
    # Display the resulting frame
    cv2.imshow('Video', frame);

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
    lastfaces = facecount;
# When everything is done, release the capture
video_capture.release();
cv2.destroyAllWindows();
