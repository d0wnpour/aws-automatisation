def read_bucket_policy(aws_s3_client, bucket_name):
  policy = aws_s3_client.get_bucket_policy(Bucket=bucket_name)

  status_code = policy["ResponseMetadata"]["HTTPStatusCode"]
  if status_code == 200:
    return policy["Policy"]
  return False