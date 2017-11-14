import sys
import boto3
from decouple import config

AWS_ACCESS_KEY = config('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

client = boto3.client(
    'rekognition',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,)

images = []
image_bytes = []

images.append(sys.argv[1])
images.append(sys.argv[2])

for image_name in images:
    try:
        imgfile = open(image_name, 'rb')
        imgbytes = imgfile.read()
        imgfile.close()
        image_bytes.append(imgbytes)
    except:
        print('There was an error opening the image')

source_image = {'Bytes': image_bytes[0]}
target_image = {'Bytes': image_bytes[1]}

response = client.compare_faces(SourceImage=source_image, TargetImage=target_image)


print(response)
