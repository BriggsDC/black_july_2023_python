import boto3 

s3 = boto3.client('s3')

bucket = 'dcbriggs-boto3-july'
key ='test_text_string.txt'

response = s3.get_object(Bucket = bucket, Key = key) #Gets the bytes of an object instead of downloading it

object_content = response['Body'].read() #Reads in a txt file
contents = object_content.decode('utf-8') #The default decode method is 'utf-8'

print(contents)