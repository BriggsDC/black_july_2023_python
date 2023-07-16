import json
import boto3

from datetime import datetime

current_date_time = datetime.now()
customer_sqs = boto3.resource('sqs', region_name = 'eu-central-1')

def lambda_handler(event, content):
    
    customer_queue = customer_sqs.get_queue_by_name(QueueName ='customer_sales_queue') #Retrieves the queue

    date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S") #Retrieves the date/time
    message = ("The trigger was executed at the following date and time: " + str(date_time) + ".") 
    
    response = customer_queue.send_message(MessageBody = message) #Forwards message to the queue

    return {
        "statusCode": 200,
        'body': json.dumps(message)
    }
