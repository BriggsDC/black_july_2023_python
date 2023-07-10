#Search 'create keypairs' in documentation. This is how you create keypairs programmatically
import boto3

import os #Enables you to change the permissions of a file

key_name = "New Function Key Pair"
file_name = 'new_function_key_pair.pem' #Dont forget to add '.pem' to the end

ec2 = boto3.client('ec2')

response = ec2.create_key_pair(
    KeyName=key_name,
)

with open(file_name, 'w') as f: #This allows you to write it directly to a file
    f.write(response["KeyMaterial"])

os.chmod(file_name, 0o400) #Changes the permissions of a file

