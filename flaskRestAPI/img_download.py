import cv2
import requests
from io import BytesIO
from PIL import Image
import numpy as np
import urllib.request

def download_img(filename):

    # # 이미지 다운로드
    # urllib.request.urlretrieve(
    #     "https://transimagetest.s3.ap-northeast-2.amazonaws.com/"+filename,
    #     filename)

    # 다운받을 이미지 url
    url = "https://transimagetest.s3.ap-northeast-2.amazonaws.com/"+filename
    res = requests.get(url)

    #Img open
    img = np.asarray(Image.open(BytesIO(res.content)))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

if __name__ == "__main__":
    download_img("temp.jpg")