#How you delete single files
#import boto3

#bucket = "dcbriggs-boto3-july"
#key = "test_text.txt"

#s3 = boto3.client('s3')

#response = s3.delete_object(
    #Bucket=bucket,
    #Key=key
#)


#Below is how you delete multiple files; method #1
#import boto3

#def delete_object(client, bucket, key): #This creates a 'delete_object function'
    #response = client.delete_object(
        #Bucket=bucket,
        #Key=key
    #)


#bucket = "dcbriggs-boto3-july"
#key = "test_text.txt"

#s3 = boto3.client('s3')

#keys = ["test_text_string.txt", "test_text.upload.txt"]

#for key in keys: 
    #delete_object(s3, bucket, key)

#Below is how you delete multiple files; method #2
#import boto3

#def delete_object(client, bucket, key): #This creates a 'delete_object function'
    #response = client.delete_object(
        #Bucket=bucket,
        #Key=key
    #)
    
    #return response

#def delete_objects(client, bucket, keys):
    
   #objects = [{'Key': key} for key in keys]
    
   #response = client.delete_objects(
        #Bucket=bucket,
        #Delete={
            #'Objects': objects
        #},
    #)

   #return response
    
#bucket = "dcbriggs-boto3-july"
#key = "test_text.txt"

#s3 = boto3.client('s3')

#keys = ["test_text_string.txt", "test_text.upload.txt"]

#delete_objects(s3, bucket, keys)

#Deleting folders **Error
#import boto3

#from list_objects import list_objects_keys

#def delete_object(client, bucket, key): #This creates a 'delete_object function'
    #response = client.delete_object(
        #Bucket=bucket,
        #Key=key
    #)
    
    #return response

#def delete_objects(client, bucket, keys):
    
   #objects = [{'Key': key} for key in keys]
    
   #response = client.delete_objects(
        #Bucket=bucket,
        #Delete={
            #'Objects': objects
        #},
    #)

   #return response
    
#if __name__ == '__main__':

    #bucket = "dcbriggs-boto3-july"

    #s3 = boto3.client('s3')

    #keys = list_objects_keys(s3, bucket, prefix = "folder_.txt_folder/")
    
    #delete_objects(s3, bucket, keys)
    
#Deleting only a single folder; NOT recursively
import boto3

from list_objects import list_objects_keys

def delete_object(client, bucket, key): #This creates a 'delete_object function'
    response = client.delete_object(
        Bucket=bucket,
        Key=key
    )
    
    return response

def delete_objects(client, bucket, keys):
    
   objects = [{'Key': key} for key in keys]
    
   response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        },
    )

   return response
    
if __name__ == '__main__':

    bucket = "dcbriggs-boto3-july"

    s3 = boto3.client('s3')
    
    prefix = "folder/foldera/"

    keys = list_objects_keys(s3, bucket, prefix = prefix)
    
    print(keys)
    
    keys = [key for key in keys if "/" not in key[len(prefix):]]
    
    print(keys)
    
    delete_objects(s3, bucket, keys)