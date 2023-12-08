import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # Si el objeto S3 no se especificó debemos usaremos el file_name 
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Subimos el archivo
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def download_file(bucket, key , file_name):
    s3 = boto3.client('s3')
    print(bucket)
    s3.download_file(Bucket=bucket, Key=key, Filename= file_name)
   
def resize_image(file_name, new_name, ratio):
    from PIL import Image
    im = Image.open(file_name)
    resized_im = im.resize((round(im.size[0]*ratio), round(im.size[1]*ratio)))
    resized_im.save(new_name)


#upload_file('portrait.jpg', 's3-web-tijuana')
#download_file('portrait_new.jpg', 's3-web-tijuana', 'portrait.jpg')