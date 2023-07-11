import json

import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    #TODO implement
    print('Hello from Lambda!')
    
    response = s3.list_buckets()
    
    bucket_names = []
    buckets = response["Buckets"]
    
    for bucket in buckets:
        print(bucket["Name"])
        bucket_names.append(bucket["Name"])
        
    return{
        'body': json.dumps(bucket_names, indent=4)
    }
