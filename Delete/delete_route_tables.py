import boto3

route_table_id = "rtb-0c769a581ed32029a" #NOT associated w/ a subnet

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId = route_table_id,
)


