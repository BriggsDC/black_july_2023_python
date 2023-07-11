#Look for "describe images" in documentatiom
import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_images(Owners = ['self']) #Insert 'self' instead of 'amazon' to see the AMIs you created

for image in response["Images"]:
    print(image["ImageId"], image["Name"], image["CreationDate"])
    
#print(response)
