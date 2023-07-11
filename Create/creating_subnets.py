import boto3

cidr_block = '12.0.1.0/24' #Increment 3rd number by 1 and last number by 12
vpc_id = 'vpc-086165851b1df0c64' #Copied/pasted from AWS VPC dashboard

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)

print(subnet["Subnet"]["SubnetId"]) #Confirm by going to VPC, clicking it's link and scroll dowm to see subnet 
