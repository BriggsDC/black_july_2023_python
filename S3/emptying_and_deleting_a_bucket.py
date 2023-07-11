#Deletes a bucket
#import boto3 #Remember, in AWS you can NOT delete a bucket thats not empty

#s3 = boto3.client('s3')

#bucket = "dcbriggs-boto3-july"

#response = s3.delete_bucket(
    #Bucket=bucket
#)

#Empties a bucket
import boto3 #Remember, in AWS you can NOT delete a bucket thats not empty

def empty_bucket(client, bucket): 
    response = client.list_objects_v2(Bucket=bucket) 
    
    if "Contents" in response:
        objects = [{'Key': content["Key"]} for content in response["Contents"]]
    
        response = client.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects': objects
            },
        )
        
        while response.get("extContinuationToken"):
            response = client.list_objects_v2(Bucket=bucket, 
                           ContinuationToken=response["NextContinuationToken"]) 
                           
            objects = [{'Key': content["Key"]} for content in response["Contents"]]   
            
            response = client.delete_objects(
                Bucket=bucket,
                Delete={
                    'Objects': objects
                },
            )

s3 = boto3.client('s3')

bucket = "dcbriggs-boto3-july"

empty_bucket(s3, bucket)

response = s3.delete_bucket(
    Bucket=bucket
)


          