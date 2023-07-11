import boto3
import os

from list_objects import list_objects_keys #Copied from 'downloading_all_of_the_objects_in_a_bucket.py'

def download_single_object(client, bucket, key, filename): #This creates a function that downloads a single object
    client.download_file(bucket, key, filename) #The bucket, the key and where youre saving it to

if __name__== '__main__':

    bucket = 'dcbriggs-boto3-july'
    key ='test_text_string.txt'
    filename = 'test_text_string.txt'

    s3 = boto3.client('s3')

    keys = list_objects_keys(s3, bucket) 
    
    for key in keys: #Iterates through keys and downloads objects
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else:
            download_single_object(s3, bucket, key, filename)
 