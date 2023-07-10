#Search documentation for 'create an image' 
import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    
    InstanceId='i-064b67b2452134c62',
    Name='Go-to AMI'
)

print(response["ImageId"])