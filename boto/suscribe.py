from s3client import sns_client

response = sns_client.subscribe(
    TopicArn="arn:aws:sns:us-east-1:162666249807:Test",
    Protocol="email",
    Endpoint="Selvin3901@gmail.com",
    ReturnSubscriptionArn=True
    )
print(response)