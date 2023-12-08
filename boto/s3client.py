# Example simplified from here
# https://github.com/HackSoftware/Django-Styleguide-Example/blob/master/styleguide_example/integrations/aws/client.py

import boto3
import credentials 

#sns_cliente = boto3.client("sns",credentials.AWS_ACCESS_KEY_ID)

def s3_get_client():
    return boto3.client(
        service_name="s3",
        aws_access_key_id=credentials.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=credentials.AWS_ACCESS_KEY,
        region_name=credentials.AWS_REGION_NAME,
        aws_session_token=credentials.AWS_SESSION_TOKEN
    )


def s3_generate_presigned_post(*, file_path: str, file_type: str):
    s3_client = s3_get_client()

    acl = credentials.AWS_DEFAULT_ACL
    expires_in = credentials.AWS_PRESIGNED_EXPIRY

    presigned_data = s3_client.generate_presigned_post(
        credentials.AWS_S3_BUCKET_NAME,
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
    
sns_client = boto3.client(
        "sns",
        aws_access_key_id=credentials.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=credentials.AWS_ACCESS_KEY,
        region_name=credentials.AWS_REGION_NAME,
        aws_session_token=credentials.AWS_SESSION_TOKEN
    )