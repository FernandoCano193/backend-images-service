from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import boto3
import pathlib
from worker import s3image
from boto import credentials
import sys
from uuid import uuid4

# Create your views here.


QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/162666249807/MyQue'

client = boto3.client('sqs')

@csrf_exempt
def upload_start(request):
    try:
        data = json.loads(request.body)
        print(data)
        # Use the data here
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    file_name = file_generate_name(data['file_name'])
    presigned_data = s3_generate_presigned_post(file_path=file_name,file_type=data['file_type'])
    print(file_name, presigned_data) 
    return JsonResponse(presigned_data)
    
@csrf_exempt
def upload_finish(request):
    image_small =""
    
    try:
        data = json.loads(request.body)
        print(data['file_name'])
        publicar()
        # 
        # Use the data here
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'message': 'Success', 'image':image_small})


def s3_generate_presigned_post(*, file_path: str, file_type: str):
    s3_client = boto3.client( service_name="s3")

    acl =  'public-read' # 'private'
    expires_in = 1000

    presigned_data = s3_client.generate_presigned_post(
        ##CAMBIAR NOMBRE SEL BOKET
        'bucketproyectoweb',
        file_path,
        Fields={
            "acl": acl,
            "Content-Type": file_type
        },
        Conditions=[
            {"acl": acl},
            {"Content-Type": file_type},
        ],
        ExpiresIn=expires_in,
    )
    return presigned_data

def file_generate_name(original_file_name):
    name = pathlib.Path(original_file_name)
    extension = name.suffix
    file_name = name.stem
    return f"original/{file_name}-{uuid4().hex}{extension}"

# def function():
#     message = client.receive_message(QueueUrl=QUEUE_URL,
#                     WaitTimeSeconds=2,
#                     )
#     if message and 'Messages' in message and message['Messages']:
#         try:
#             receipt_handle = message['Messages'][0]['ReceiptHandle']
#             body =  json.loads(message['Messages'][0]['Body'])
#             bucket_name = body['Records'][0]['s3']['bucket']['name']
#             key = body['Records'][0]['s3']['object']['key']
#             filename = key.split('/')[-1]
#             message_id =  message['Messages'][0]['MessageId']
#             print(message_id,bucket_name, key, receipt_handle)
#             #ver el codigo de download_file
#             s3image.download_file(bucket_name, key, 'image.jpg')
#             print('imagen recibida')
#             s3image.resize_image('image.jpg','new.jpg')
#             print('imagen transformada') 
#             s3image.upload_file('new.jpg', bucket_name,
#                      f'small/{filename}',  extra_args={'ACL': 'public-read'}) 
#             print('imagen almacenada')
#             client.delete_message( QueueUrl=QUEUE_URL, ReceiptHandle=receipt_handle )
#             print('mensaje eliminado')
#         except Exception as e:
#             print(e)
#             client.delete_message( QueueUrl=QUEUE_URL, ReceiptHandle=receipt_handle )

def publicar():
    sns_client = boto3.client(
        "sns",
        aws_access_key_id=credentials.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=credentials.AWS_ACCESS_KEY,
        region_name=credentials.AWS_REGION_NAME,
        aws_session_token=credentials.AWS_SESSION_TOKEN
    )
    sns_client.publish(
    TopicArn="arn:aws:sns:us-east-1:162666249807:Test",
    Message="Foto subida con exito"
    )