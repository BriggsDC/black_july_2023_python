import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

for routeTable in response["RouteTables"]:
    print(routeTable["VpcId"], routeTable["RouteTableId"]) #Note that subnets can be explicitly associated w/ a route table
    
    for association in routeTable['Associations']:
        print(association["RouteTableAssociationId"]) 
        if "SubnetID" in association:
            print(association["SubnetId"])
            
    for route in routeTable["Routes"]:
        print(route["DestinationCidrBlock"], route["GatewayId"])
        