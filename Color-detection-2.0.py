# Offical release by Nadohoi
# Ver 2.0
# Only For Raspberry Pi

# Importing all modules
import cv2 # pip3 install opencv (must be version 4)
import numpy as np # pip3 install numpy
import threading
import board
import adafruit_mlx90614
import busio as io

# Specifying upper and lower ranges of color to detect in hsv format
lower_red = np.array([0, 60, 60])
upper_red = np.array([6, 255, 255])     # (These rangers will detect Red)
lower_orange = np.array([5, 100, 150])
upper_orange = np.array([13, 225, 225]) # (These ranges will detect Orange)
lower_green = np.array([55, 65, 55])
upper_green = np.array([85, 255, 255])  # (These ranges will detect Green)

# Locating mlx90614's i2c
i2c = io.I2C(board.SCL,board.SCA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

# Creating definition for threading
def get_red():
    mask = cv2.inRange(img, lower_orange, upper_orange) # Masking the image to find our color
    mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
    
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 500:
                    cv2.putText(video, "STOP", (cx + 200, cy + 230), 0, 1, (255, 255, 255), 4)
                    x, y, w, h = cv2.boundingRect(mask_contour)
                    cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) # Drawing rectangle

def get_orange():
    mask = cv2.inRange(img, lower_orange, upper_orange) # Masking the image to find our color
    mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
    
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 500:
                    cv2.putText(video, "STOP", (cx + 200, cy + 230), 0, 1, (255, 255, 255), 4)
                    x, y, w, h = cv2.boundingRect(mask_contour)
                    cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) # Drawing rectangle

def get_green():
    mask2 = cv2.inRange(img, lower_green, upper_green)
    mask_contours2, hierarchy2 = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image
    
    if len(mask_contours2) != 0:
        for mask_contour in mask_contours2:
            if cv2.contourArea(mask_contour) > 150:
                cv2.putText(video, "GO", (cx + 200, cy + 230), 0, 1, (255, 255, 255), 4)
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) # Drawing rectangle

def get_temp():
    obj_temp = mlx.object_temperature
    amb_temp = mlx.ambient_temperature

# Capturing webcam footage
webcam_video = cv2.VideoCapture(0)
webcam_video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam_video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize frame rate calculation
frame_rate_calc = 1
freq = cv2.getTickFrequency()

while True:
    # Start timer (for calculating frame rate)
    t1 = cv2.getTickCount()
    
    success, video = webcam_video.read() # Reading webcam footage
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format
    height, width, _ = img.shape
    cx = int(width / 2)
    cy = int(height / 2)
    
    thread1 = threading.Thread(target=get_red())
    thread2 = threading.Thread(target=get_orange())
    thread3 = threading.Thread(target=get_green())
    thread4 = threading.Thread(target=get_temp())
    
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    
    # Draw framerate in corner of frame
    cv2.putText(video, "FPS: {0:.2f}".format(frame_rate_calc), (cx - 300 , cy + 230), 0, 1, (255,255,255), 4)
    cv2.putText(video, "TEMP: " + str(obj_temp), (cx - 300 , cy - 230), 0, 1, (255,255,255), 4)          
    
    cv2.imshow("window", video) # Displaying webcam image
    
    # Calculate framerate
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc= 1/time1

    key = cv2.waitKey(1)
    
    if key == ord("q"):
        webcam_video.close()
        cv2.destroyAllWindows()
        break
