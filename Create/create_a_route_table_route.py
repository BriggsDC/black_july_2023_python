import boto3

route_table_id = "rtb-0c769a581ed32029a"
internet_gateway_id = "igw-0aeeff88a200e2f44"

ec2 = boto3.client('ec2')

ec2.create_route( #'response' not necessary if example on consists of "ResponseMetadata"
    DestinationCidrBlock = "0.0.0.0/0", #Destination CIDR block is usually 0
    GatewayId = internet_gateway_id,
    RouteTableId = route_table_id,
)

