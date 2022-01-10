
AWS_ACCESS_KEY = "AKIATPTBFRP3W2Q6EA7C"
AWS_SECRET_ACCESS_KEY = "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"
AWS_S3_BUCKET_REGION = "ap-northeast-2"
AWS_S3_BUCKET_NAME = "transimagetest"

#
# s3 = boto3.session.Session('s3', AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_S3_BUCKET_REGION)
# s3.download_file(AWS_S3_BUCKET_NAME, '/temp.jpg', 'temp.jpg')
#
#
import boto3
s3 = boto3.resource('s3', AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_S3_BUCKET_REGION)
s3.Object(AWS_S3_BUCKET_NAME, 'temp.jpg').get_object('/temp.jpg')

# import boto3
#
# s3 = boto3.client('s3')
