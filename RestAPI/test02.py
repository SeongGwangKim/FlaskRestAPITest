import boto3
import json

with open("C:/Users/ksk30/.aws/credentials.json") as f:
    json_loaded = json.load(f)
    ACCESS_KEY = json_loaded["aws_access_key_id"]
    SECRET_ACCESS_KEY = json_loaded["aws_secret_access_key"]



AWS_ACCESS_KEY = "AKIATPTBFRP3W2Q6EA7C"
AWS_SECRET_ACCESS_KEY = "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"
AWS_S3_BUCKET_REGION = "ap-northeast-2"
AWS_S3_BUCKET_NAME = "transimagetest"

import boto3
response = boto3.client.create_access_key(
    UserName='OliverKim'
)
s3 = boto3.resource('s3')
s3.meta.client.download_file('AWS_S3_BUCKET_NAME', 'temp.jpg', '/temp.jpg')