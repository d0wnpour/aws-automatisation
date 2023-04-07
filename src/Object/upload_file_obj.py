def upload_file_obj(aws_s3_client, filename, bucket_name):
  with open(filename, "rb") as file:
    aws_s3_client.upload_fileobj(file, bucket_name, "hello_obj.txt")
