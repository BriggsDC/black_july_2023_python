import boto3

route_table_id = 'rtb-0c769a581ed32029a' #Be sure to use one NOT already associated w/ the VPC

subnet_id = 'subnet-0433b5af123d1b4ad' #You can copy/paste from AWS "resource map" page

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId = route_table_id,
    SubnetId = subnet_id,
)

print(association["AssociationId"])