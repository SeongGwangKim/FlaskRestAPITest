import boto3

s3 = boto3.client('s3')
with open('../flaskRestAPI/temp1.jpg', 'wb') as f:
    s3.download_fileobj('transimagetest', 'temp.jpg', f)

#
# import boto3
#
# s3 = boto3.client('s3')
# s3.download_file('transimagetest', 'temp.jpg', 'temp.jpg')