import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='Security Group from Boto3',
    GroupName='Boto3-security-group',
    VpcId='vpc-032c043067dfccc1a',
)

print(response["GroupId"])