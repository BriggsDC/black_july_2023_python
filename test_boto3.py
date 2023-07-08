import boto3 #Install Boto3 into Python; use 'pip install boto3' to nstall modules for Python. Use 'import' to gain access to things not native to Python
import json #Makes output more readable

session = boto3.Session() #Acquires temp session for you to access AWS

#s3 = boto3.client('s3') #The 'client' is what you use to integrate w/ the AWS API
s3_client = session.client('s3')

#s3 = boto3.resource('s3')
#s3 = session.resource('s3')

response = s3_client.create_bucket(
    Bucket='dcb-070823-boto3-test',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'
    },
)
print(json.dumps(response, indent=2))