import boto3

AWS_ACCESS_KEY = "AKIATPTBFRP3W2Q6EA7C"
AWS_SECRET_ACCESS_KEY = "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"
AWS_S3_BUCKET_REGION = "ap-northeast-2"
AWS_S3_BUCKET_NAME = "transimagetest"

client = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_S3_BUCKET_REGION
                      )
response = client.list_buckets() # bucket 목록
print(response)

###################################################

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_S3_BUCKET_REGION
)

s3 = session.resource('s3')  # s3에 대한 권한 및 상태를 s3(변수)에 저장

for bucket in s3.buckets.all():
    print(bucket.name)

AWS_BUCKET_NAME = "transimagetest"

buckets = s3.Bucket(name=AWS_BUCKET_NAME)
print(buckets)
# 출력: s3.Bucket(name='aws-jihoon-testserver')

for obj in buckets.objects.all():
    print(obj)
    print(obj.key)

#########################################

AWS_BUCKET_NAME = "transimagetest"
object_key = "temp.jpg"

s3 = boto3.resource('s3')
object_ = s3.Object(AWS_BUCKET_NAME, object_key)

# output
img = s3.Object(bucket_name='transimagetest', key='temp.jpg').download_file('/temp/temp.jpg')
print(img)
# session = boto3.Session()
# print("session", session)