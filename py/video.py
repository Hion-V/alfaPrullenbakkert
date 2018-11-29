import numpy as np
import cv2

a = "nee";
print(a);
cap = cv2.VideoCapture(0);
cv2.namedWindow("test");
        #image = camera.read();
        #cv2.imwrite('opencv.png', image);
        #del(camera);
while True:
        #capture frame-by-frame
        ret, frame = cap.read();

        #Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

        #Display the resulting frame
        cv2.imshow('frame',gray);
        if cv2.waitKey(1) & 0xff == ord('q'):
                break



cap.release();          

cv2.destoyAllWindows();