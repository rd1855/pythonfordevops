# import boto3

# s3_obj = boto3.resource('s3')
# #print(dir(s3_obj))
# # print(s3_obj.buckets.all())
# for bucket in s3_obj.buckets.all():
#     print(bucket.name)

def show_buckets(s3_obj):
    for bucket in s3_obj.buckets.all():
        print(bucket.name)
        
def upload_file(s3_obj, bucket_name, file_path,key_name ):
    file_data = open(file_path, 'rb')
    s3_obj.Bucket(bucket_name).put_object(Key=key_name, Body=file_data)
    file_data.close() 
    print(f"File {file_path} uploaded to bucket {bucket_name} with key {key_name}")
    
def list_files(s3_obj, bucket_name):
    print(f"Files in bucket {bucket_name} are:")
    bucket = s3_obj.Bucket(bucket_name)
    for obj in bucket.objects.all():
        print(f" - {obj.key}")

def create_bucket(s3_obj, bucket_name, CreateBucketConfiguration=None):
    s3_obj.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration=CreateBucketConfiguration
    )
    print(f"Bucket {bucket_name} created in region {CreateBucketConfiguration['LocationConstraint']}")