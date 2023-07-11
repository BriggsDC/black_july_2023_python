#import boto3

#s3 = boto3.client('s3')

#response = s3.list_objects_v2(Bucket="dcbriggs-boto3-july", Prefix="test_text") #'Prefix' is a filter that searches the folders

#Below is another option
#response = s3.list_objects_v2(Bucket="dcbriggs-boto3-july") 

#for content in response ["Contents"]:
    #if(".txt" in content["Key"][-4:]): #This filters and returns anything w/ that has the last 4 characters ending in '.txt'
        #print(content["Key"]) #This lists recursively all of the things in your S3 bucket
        
        
#Below is an alternative way to do it as a function
import boto3

def filter_objects_extension(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket) 
    for content in response ["Contents"]:
        if(extension in content["Key"][-(len(extension)):]): #This filters and returns anything w/ that has the last 4 characters ending in '.txt'
          keys.append(content["Key"]) #This lists recursively all of the things in your S3 bucket
          
    return keys
    
def list_objects_keys(client, bucket, prefix=""):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix) 
    for content in response ["Contents"]:
        keys.append(content["Key"]) #This lists recursively all of the things in your S3 bucket
          
    return keys  
    
s3 = boto3.client('s3')

response = list_objects_keys(s3, "dcbriggs-boto3-july") #You can add 'folder/' as a test
print(response)

response = filter_objects_extension(s3, "dcbriggs-boto3-july", ".txt") 
print(response)
    