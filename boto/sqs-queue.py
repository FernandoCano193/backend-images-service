import boto3
client = boto3.client('sqs')
client.list_queues()

message_body = {
    'key1': 'value1',
    'key2': 'value2',
        }
        
import json
message_string = json.dumps(message_body)
message_string
client.send_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/052353881089/MyQueue',MessageBody=message_string)
client.receive_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/052353881089/MyQueue')