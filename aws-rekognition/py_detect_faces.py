import sys
import boto3
from decouple import config

AWS_ACCESS_KEY = config('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

client = boto3.client(
    'rekognition',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,)

image_name = sys.argv[1]

try:
    imgfile = open(image_name, 'rb')
    imgbytes = imgfile.read()
    imgfile.close()
except:
    print('There was an error opening the image')

imgobj = {'Bytes': imgbytes}

response = client.detect_faces(Image=imgobj, Attributes=['ALL'])

print(response)
