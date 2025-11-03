import boto3
from aws_wrapper import show_buckets , upload_file, list_files, create_bucket

s3_obj = boto3.resource('s3')
file_path = 'my_text.txt'

show_buckets(s3_obj)
upload_file(s3_obj,'pfd-rapper', file_path, 'my_text.txt')
list_files(s3_obj,'pfd-rapper')
#create_bucket(s3_obj,'pfd-rapper-new-2024','us-west-2')

