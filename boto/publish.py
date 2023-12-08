from s3client import sns_client

response = sns_client.publish(
    TopicArn="arn:aws:sns:us-east-1:162666249807:Test",
    Message="Foto subida con exito"
    )
print(response)