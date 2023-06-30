# import the necessary packages
from imutils.video import WebcamVideoStream
from imutils.perspective import four_point_transform
import imutils, threading, cv2, os, sys
import numpy as np

def get_red():
    mask = cv2.inRange(img_hsv, lower_red, upper_red) # Masking the image to find our color
    mask = cv2.UMat(mask)
    mask_contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 150:
                cv2.putText(img, "STOP", (250, 250), 0, 1, (255, 255, 255), 4)
                #x, y, w, h = cv2.boundingRect(mask_contour)
                #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3) # Drawing rectangle

def get_orange():
    mask2 = cv2.inRange(img_hsv, lower_orange, upper_orange) # Masking the image to find our color
    mask2 = cv2.UMat(mask2)
    mask_contours2, _2 = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
    if len(mask_contours2) != 0:
        for mask_contour2 in mask_contours2:
            if cv2.contourArea(mask_contour2) > 150:
                cv2.putText(img, "STOP", (250, 250), 0, 1, (255, 255, 255), 4)
                #x, y, w, h = cv2.boundingRect(mask_contour)
                #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3) # Drawing rectangle

def get_green():
    mask3 = cv2.inRange(img_hsv, lower_green, upper_green)
    mask3 = cv2.UMat(mask3)    
    mask_contours3, _3 = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image 
    if len(mask_contours3) != 0:
        for mask_contour3 in mask_contours3:
            if cv2.contourArea(mask_contour3) > 150:
                cv2.putText(img, "GO", (250, 250), 0, 1, (255, 255, 255), 4)
                #x, y, w, h = cv2.boundingRect(mask_contour)
                #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3) # Drawing rectangle
        
def QRCode():
    try:
        data, bbox, _ = detector.detectAndDecode(img)
        return data, bbox
    except:
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

def Transform():
    index_point = np.int32(bbox)
    rect = four_point_transform(img, index_point.reshape(4, 2))
    return rect

lower_red = np.array([3, 60, 60])
upper_red = np.array([5, 255, 255])     
lower_orange = np.array([5, 100, 150])
upper_orange = np.array([88, 255, 255]) 
lower_green = np.array([69, 63, 97])
upper_green = np.array([135, 255, 255])  

cap = WebcamVideoStream(src = 0).start()
FRAME_RATE_CALC= 1
detector = cv2.QRCodeDetector()

while True:
    freq = cv2.getTickFrequency()
    t1 = cv2.getTickCount() 
    img = cap.read()
    img = imutils.resize(img, width=400)
    
    data, bbox = QRCode()
    
    if data != "":
        rect = Transform()
        img_hsv = cv2.cvtColor(rect, cv2.COLOR_BGR2HSV)
        
        th1 = threading.Thread(target=get_red())
        th2 = threading.Thread(target=get_orange())
        th3 = threading.Thread(target=get_green()) 
            
        th1.start()
        th2.start()
        th3.start()
        
        th1.join()
        th2.join()
        th3.join()   

    cv2.putText(img, "FPS: %s" %FRAME_RATE_CALC, (230 , 275), 0, 1, (255,255,255), 3)  
    
    cv2.imshow("Health Code Detection", img)
    
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    FRAME_RATE_CALC= 1//time1
        
    if cv2.waitKey(1) == ord("q"):
        exit()