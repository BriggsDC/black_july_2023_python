import boto3

customer_sqs = boto3.resource('sqs', region_name='eu-central-1') 

customer_queue = customer_sqs.create_queue(QueueName = 'customer_sales_queue') 

print("The following SQS queue", customer_queue.attributes['QueueArn'].split(':')[-1], "has been created and the URl is as follows: ", customer_queue.url)

