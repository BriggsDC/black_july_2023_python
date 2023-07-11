import boto3

subnet_id = 'subnet-0433b5af123d1b4ad'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)

