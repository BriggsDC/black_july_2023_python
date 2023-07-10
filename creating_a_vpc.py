import boto3

ec2 = boto3.client('ec2')

vpc = ec2.create_vpc(CidrBlock='12.0.0.0/16') #Use CIDR.xyz https://cidr.xyz to decide what CIDR to use 

print(vpc["Vpc"] ["VpcId"])