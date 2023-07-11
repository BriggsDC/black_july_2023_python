#Search 'authorize security group ingress ' in documentation' this changes the rules for things going 'into' the SG
import boto3

security_group_id = "sg-0a53637de073fd1cf" #Copied from script ran in "creating security group"

ec2 = boto3.client('ec2')

response = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'FromPort': 22, #Port 22 = SSH
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0', #Allow from anywhere
                },
            ],
            'ToPort': 22,
        },
        {
            'FromPort': 80, #Port 80 = HTTPS
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0', #Allow from anywhere
                },
            ],
            'ToPort': 80,
        },
    ],
)

print(response)