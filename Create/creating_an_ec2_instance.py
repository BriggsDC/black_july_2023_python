#Search documention for 'run instances' 
import boto3

ami_id = 'ami-03479dcd7e8bf8590'
key_pair_name = 'Key from boto3'
security_group_id = 'sg-0a53637de073fd1cf'

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
       security_group_id
    ]
)

print(response["Instances"][0]["InstanceId"])