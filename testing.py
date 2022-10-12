from imutils.perspective import four_point_transform
import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    return_value, inputimage = camera.read()
    cv2.imshow('img', inputimage)
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite('poke.png', inputimage)
        break

cv2.destroyAllWindows()

# 加载图片
src_image = cv2.imread("poke.png")
# 实例化
qrcoder = cv2.QRCodeDetector()
# qr检测并解码
codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(src_image)
# 绘制qr的检测结果
cv2.drawContours(src_image, [np.int32(points)], 0, (0, 0, 255), 2)

cv2.imshow("result", src_image)
cv2.waitKey(0)


#rect = four_point_transform(src_image, np.int32(points))
#cv2.imwrite('poke_rect.png', rect)
#cv2.imshow("rect", rect)




#cv2.namedWindow("img")

#while True:
    #cv2.imshow('img', image)
    #if cv2.waitKey() == ord('q'):
        #break


#cv2.waitKey(0)
#cv2.destroyAllWindows()
        
