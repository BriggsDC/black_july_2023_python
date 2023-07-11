import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_internet_gateways()

for ig in response["InternetGateways"]:
    print(ig["InternetGatewayId"])
    
    for attachment in ig["Attachments"]: #Lists VPCs attached to the 'ig'/Internet Gateway
        print(attachment["VpcId"], attachment["State"])
        
#print(response)