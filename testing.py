from imutils.perspective import four_point_transform
import cv2
import numpy as np
import sys
import time

def four_point(x, y):
    global four_points
    four_points.append([x, y])

while True:
    camera = cv2.VideoCapture(0)
    return_value, inputimage = camera.read()
    if cv2.waitKey() == ord('q'):
        cv2.imwrite('poke.png', inputimage)
        break

img_path = 'poke.png'
image = cv2.imread("poke.png")
det = cv2.QRCodeDetector()
info, box_coordinates, _ = det.detectAndDecode(img_path)
four_points = [tuple(box_coordinates[0][i]), tuple(box_coordinates[0][(i+1) % n])]

cv2.namedWindow("img")

while True:
    cv2.imshow('img', image)
    if cv2.waitKey() == ord('q'):
        break

# print(four_points)
rect = four_point_transform(image, np.array(four_points))
cv2.imwrite('poke_rect.png', rect)
cv2.imshow("rect", rect)
cv2.waitKey(0)
cv2.destroyAllWindows()
