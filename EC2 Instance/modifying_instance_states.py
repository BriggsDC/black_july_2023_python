#Search documentation for 'stop instance' 'start instance' 'terminate instance'
import boto3

def stop_instance(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id
        ],
    )

    print(instance_id, "Stopped")
    
def start_instance(client, instance_id):
    response = client.start_instances(
        InstanceIds=[
            instance_id 
       ],
   )
   
    print(instance_id, "Started")

def terminate_instance(client, instance_id):
    response = client.terminate_instances(
        InstanceIds=[
            instance_id 
       ],
   )
   
    print(instance_id, "Terminated")

if __name__=='__main__':
    instance_id = "i-0081bcaf1a5444289"

    ec2 = boto3.client('ec2')
    terminate_instance(ec2, instance_id) #Note here is where you'd annotate 'start, stop, terminate'

#print(response)