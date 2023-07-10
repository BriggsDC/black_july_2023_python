import boto3

internet_gateway_id = 'igw-0aeeff88a200e2f44' #Copied from AWS as 'detached'
vpc_id = 'vpc-086165851b1df0c64'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId = internet_gateway_id,
    VpcId = vpc_id,
)

