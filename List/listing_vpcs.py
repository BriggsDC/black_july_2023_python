#Listing VPC ID, CIDR,
#import boto3

#ec2 = boto3.client('ec2')

#response = ec2.describe_vpcs()

#for vpc in response["Vpcs"]: #Pay attention and avoid unecessary capitalization; use the JSON Formatter
    #print(vpc["VpcId"], vpc["CidrBlock"], vpc["IsDefault"])

#for vpc in response["Vpcs"]:#Pulls the 'tag' where the VPC name is nested
    #if "Tags" in vpc:
        #for tag in vpc["Tags"]:
            #if "Name" == tag['Key']:
                #print(tag["Value"])
                
#Listing default VPC; use a filter
import boto3

def get_vpc_information(client, filters=[]):
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response["Vpcs"]: #Pay attention and avoid unecessary capitalization; use the JSON Formatter
        print(vpc["VpcId"], vpc["CidrBlock"], vpc["IsDefault"])
        
def get_vpc_name(client, filters=[]):
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response["Vpcs"]: #Pay attention and avoid unecessary capitalization; use the JSON Formatter
        if "Tags" in vpc:
            for tag in vpc["Tags"]:
                if "Name" == tag['Key']:
                    print(tag["Value"])       

if __name__=='__main__':
    ec2 = boto3.client('ec2')
                
    Filters=[{'Name': 'isDefault', 'Values': ['true',]},] #This is a function, use lowercase here
    
    get_vpc_information(ec2)
    get_vpc_information(ec2, Filters)