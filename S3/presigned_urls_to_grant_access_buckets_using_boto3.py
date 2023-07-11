import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': 'dcbriggs-boto3-july', 'Key': 'test_text.txt'}, ExpiresIn=300) #This is seconds; 5 min  = 300

print(response)