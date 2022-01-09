

import cv2
import urllib.request

urllib.request.urlretrieve(
    'https://transimagetest.s3.ap-northeast-2.amazonaws.com/temp.jpg',
    "../flaskRestAPI/temp1.jpg")

img = cv2.imread("../flaskRestAPI/temp1.jpg")
cv2.imshow('res', img)
cv2.waitKey(0)
print(img)
