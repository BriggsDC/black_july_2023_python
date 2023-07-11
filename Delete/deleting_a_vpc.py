import boto3

vpc_id = 'vpc-086165851b1df0c64'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)

