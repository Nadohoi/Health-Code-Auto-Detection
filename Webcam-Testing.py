# Offical release by Nadohoi
# Ver 1.0

# Importing all modules
import cv2
import numpy as np

while True:
    success, video = webcam_video.read() # Reading webcam footage
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format
    height, width, _ = img.shape
    
    cv2.imshow("window", video) # Displaying webcam image

    key = cv2.waitKey(1)
    
    if key == ord("q"):
        webcam_video.close()
        cv2.destroyAllWindows()
        break
