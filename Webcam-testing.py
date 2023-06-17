# Offical release by Nadohoi
# Ver 1.0

# Importing all modules
import cv2
import numpy as np

webcam_video = cv2.VideoCapture(0)
webcam_video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam_video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    success, video = webcam_video.read() # Reading webcam footage   
    cv2.imshow("window", video) # Displaying webcam image

    key = cv2.waitKey(1)
    
    if key == ord("q"):
        webcam_video.close()
        cv2.destroyAllWindows()
        break
