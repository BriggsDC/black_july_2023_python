#Search documentation for 'deregister image'
import boto3

ec2 = boto3.client('ec2')

response = ec2.deregister_image(
    ImageId='ami-03479dcd7e8bf8590'
)
