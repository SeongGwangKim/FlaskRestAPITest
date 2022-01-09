import io

import boto3

AWS_ACCESS_KEY = "AKIATPTBFRP3W2Q6EA7C"
AWS_SECRET_ACCESS_KEY = "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"
AWS_S3_BUCKET_REGION = "ap-northeast-2"
AWS_S3_BUCKET_NAME = "transimagetest"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
s3 = session.resource("s3", region_name="ap-northeast-2")
bucket = s3.Bucket("transimagetest")
object = bucket.Object(AWS_S3_BUCKET_NAME)
file_stream = io.BytesIO()
object.download_file('temp.jpg')
