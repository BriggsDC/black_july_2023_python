import boto3

route_table_id = 'rtb-0c769a581ed32029a' #Not viewable in AWS; you'll have to retrieve programmatically

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id 
    ],
)

for association in response["RouteTables"][0]["Associations"]:
    if not association["Main"]: #This means if it false, do the bext line
        association_id = association["RouteTableAssociationId"]
        print(association_id)
            
        ec2.disassociate_route_table( #'Disassociates' <for documentation purposes> the route table 
            AssociationId = association_id,
        )


