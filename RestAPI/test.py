from flask import Flask, app, request

from RestAPI.s3_connection import *
from RestAPI.s3_connection import AWS_S3_BUCKET_NAME, AWS_S3_BUCKET_REGION

# with open("C:/Users/ksk30/.aws/credentials.json") as f:
#     json_loaded = json.load(f)
#     ACCESS_KEY = json_loaded["aws_access_key_id"]
#     SECRET_ACCESS_KEY = json_loaded["aws_secret_access_key"]

app = Flask(__name__, static_folder='static')
s3 = s3_connection()


@app.route('/fileUpload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save("./temp.png")

    ret =s3_get_object(s3, AWS_S3_BUCKET_NAME, "./temp.jpg", ".temp.jpg")
    print(ret)
    if ret:
        print("파일 저장 성공")
    else:
        print("파일 저장 실패")