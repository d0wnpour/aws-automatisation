import boto3

def delete_object(object_name, bucket_name):
    s3 = boto3.client("s3")
    s3.delete_object(Bucket=bucket_name, Key=object_name)
    print(f"Object {object_name} deleted from bucket {bucket_name}.")