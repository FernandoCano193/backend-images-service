import configparser
import subprocess
import os

def get_aws_config():
    config = configparser.ConfigParser()
    config.read('/home/ec2-user/.aws/credentials')
    
    aws_config = {
     'AWS_ACCESS_KEY_ID':config['default']['aws_access_key_id'],
     'AWS_ACCESS_KEY': config['default']['aws_secret_access_key'], 
     'AWS_SESSION_TOKEN': config['default']['aws_session_token'],
     'AWS_REGION_NAME': config['default']['region']
     }
    return aws_config
    
aws_config = get_aws_config()   

AWS_ACCESS_KEY_ID = aws_config['AWS_ACCESS_KEY_ID']
AWS_ACCESS_KEY = aws_config['AWS_ACCESS_KEY']
AWS_REGION_NAME = aws_config['AWS_REGION_NAME']
AWS_SESSION_TOKEN = aws_config['AWS_SESSION_TOKEN']
AWS_DEFAULT_ACL = 'private'
AWS_PRESIGNED_EXPIRY = 10
AWS_S3_BUCKET_NAME = 's3-web-tijuana'