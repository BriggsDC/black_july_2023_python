import boto3

ec2_resource = boto3.resource('ec2') 

ec2_instances = ec2_resource.create_instances( 
  
    MinCount = 3,
    MaxCount = 3,
    ImageId = 'ami-0a7fae6941864b627',
    InstanceType ='t2.micro',
    KeyName = 'New Function Key Pair',
    TagSpecifications =[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name','Value': 'Dev Instance Server'}, 
            {'Key': 'Environment','Value': 'Dev'}]
            
        }
        ]
    )

print(len(ec2_instances), "The following Development EC2 instances have been created:\n ", ec2_instances.id)