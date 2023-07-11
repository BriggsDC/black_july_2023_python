#Look for "describe instance type" in the online documentation
import boto3


ec2 = boto3.client('ec2')

response = ec2.describe_instance_types(
     Filters=[
        {
            'Name': 'free-tier-eligible',
            'Values': [
                'true',
            ]
        },
    ]
    
    )

for instanceType in response["InstanceTypes"]:
    print(instanceType["InstanceType"], instanceType["FreeTierEligible"])
    
#print(response)