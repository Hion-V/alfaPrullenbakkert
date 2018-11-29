import cv2

a = "nee";
print(a);
camera = cv2.VideoCapture(0);
img_counter = 0;
cv2.namedWindow("test");
        #image = camera.read();
        #cv2.imwrite('opencv.png', image);
        #del(camera);
while True:
        ret, frame = camera.read();
        cv2.imshow("test", frame);
        k = cv2.waitKey();
        if not ret:
                break;
        elif k == 27:
                #ESC PRESSED
                p8rint("Escape hit, closing...");
                break;
        elif k == 32:
                #SPACE PRESSED
                img_name = "opencv_frame_{}.png".format(img_counter);
                cv2.imwrite(img_name, frame);
                print("{} written!".format(img_name));
                img_counter +=1;
        sleep(10);

camera.release();          

cv2.destoyAllWindows();
