import boto3

s3 = boto3.client('s3')

#with open("test_text.txt", 'rb') as f: #'rb' means read this in as bytes and 'f' for file
    #s3.put_object(Bucket="dcbriggs-boto3-july", Key="test_text.txt", Body=f, ContentType="text/plain")

#Below is another way w/ 'ExtraArgs' Extra Arguments
s3.upload_file('test_text.txt', 'dcbriggs-boto3-july', 'test_text.upload.txt', ExtraArgs={'ContentType':'text/plain'})