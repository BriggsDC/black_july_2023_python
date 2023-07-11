#When deleting things a VPC, delete everything in the reverse order they were created

import boto3

route_table_id = 'rtb-0c769a581ed32029a'

ec2 = boto3.client('ec2')

ec2.delete_route(
    DestinationCidrBlock = '0.0.0.0/0',
    RouteTableId = route_table_id,
)

