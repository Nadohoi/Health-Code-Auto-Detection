# Release Update by Nadohoi
# Ver 2.0

# Importing all modules
from imutils.perspective import four_point_transform
import cv2
import numpy as np

# Capturing webcam footage
cap = cv2.VideoCapture(0)

# Taking a picture
while True:
    success, frame = cap.read()

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(frame)
    if bbox is not None:
        index_point = np.int32(bbox)
        rect = four_point_transform(frame, index_point.reshape(4, 2))
        
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        out = cv2.imwrite("capture.png", rect)
        break

cap.release()
cv2.destroyAllWindows()

winName = "colors"

def nothing(x):
    pass

# Reading the image taken
img_original = cv2.imread("capture.png")
img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)

# Creating window
cv2.namedWindow("colors")

# Create trackbars to adjust upper and lower ranges of color to detect in hsv format
cv2.createTrackbar('LowerbH', "colors", 55, 255, nothing)
cv2.createTrackbar('LowerbS', "colors", 65, 255, nothing)
cv2.createTrackbar('LowerbV', "colors", 55, 255, nothing)
cv2.createTrackbar('UpperbH', "colors", 85, 255, nothing)

while(1):
    lowerbH = cv2.getTrackbarPos('LowerbH', "colors")
    lowerbS = cv2.getTrackbarPos('LowerbS', "colors")
    lowerbV = cv2.getTrackbarPos('LowerbV', "colors")
    upperbH = cv2.getTrackbarPos('UpperbH', "colors")

    img_target = cv2.inRange(img_original, (lowerbH, lowerbS, lowerbV), (upperbH, 255, 255))
    
    img_specifiedColor = cv2.bitwise_and(img_original, img_original, mask = img_target)
    cv2.imshow(winName, img_specifiedColor)
    
    if cv2.waitKey(1) == ord("q"):
        break
    
cv2.destroyAllWindows()
