import json

import boto3

ec2_resource = boto3.resource('ec2', region_name ='eu-central-1')

def lambda_handler(event, context):
    ec2_instances = ec2_resource.instances.all() #Creates iteration of each instance

    for ec2_instance in ec2_instances: #Loops through all instances
        ec2_instance_state = ec2_instance.state["Name"] #Retrieves the instance state
        tag = ec2_instance.tags #Retrieves the instance tag
    
        for tag in ec2_instance.tags:
            if ("Dev" == tag['Value']) & (ec2_instance_state == 'running'): #Confirms if instance is running and if tag reads 'Dev'
                stop_ec2_instance = ec2_instance.stop() #Stops instance once condition is satisfied
            
                print('The following EC2 instance hase been stopped: ' + str(ec2_instance.id))
    
    return "success"