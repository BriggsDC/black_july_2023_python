import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_security_groups()

for sg in response["SecurityGroups"]:
    print(sg["GroupId"], sg["VpcId"], sg["GroupName"], sg["Description"])
    
    for permission in sg["IpPermissions"]:
        if "FromPort" in permission:
            print(permission["FromPort"])
            
        if "IpProtocol" in permission:
            print(permission["IpProtocol"])
            
        if "ToPort" in permission:
            print(permission["ToPort"])
            
        if "IpRanges" in permission:
            for iprange in permission["IpRanges"]: #Another way to say 'or'
                print(iprange["CidrIp"])
                
#print(response)
