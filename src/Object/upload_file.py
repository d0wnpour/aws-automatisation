def upload_file(aws_s3_client, filename, bucket_name):
  response = aws_s3_client.upload_file(filename, bucket_name, "hello.txt")
  status_code = response["ResponseMetadata"]["HTTPStatusCode"]
  if status_code == 200:
    return True
  return False