import os

from flask import Flask, jsonify, request
from flaskRestAPI.img_download import download_img
from flaskRestAPI.trans_esrgan import preprocess_image
from flaskRestAPI.transimage import transfer_image
from flaskRestAPI.upload_test import upload_file

app = Flask(__name__)


@app.route('/transimage', methods=['POST'])
def transimage():
    data = request.get_json()[0]
    file_name = data["origin"]
    print(file_name)

    #이미지 다운로드(임시 저장)
    img = download_img(file_name)
    # 이미지 변환
    # transfer_image(img, file_name)
    preprocess_image(img, file_name)


    # json에 보내줄 이름
    rev_file_name = "rev_" + file_name
    response = {'results': rev_file_name}
    upload_file(rev_file_name)
    os.remove(rev_file_name)

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)


