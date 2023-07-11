import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-0a53637de073fd1cf',
)

print(response)
