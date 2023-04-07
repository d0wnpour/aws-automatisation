from Bucket.Policy.multiple_policy import multiple_policy
from Bucket.Policy.public_read_policy import public_read_policy

def assign_policy(aws_s3_client, policy_function, bucket_name):
  policy = None
  if policy_function == "public_read_policy":
    policy = public_read_policy(bucket_name)
  elif policy_function == "multiple_policy":
    policy = multiple_policy(bucket_name)

  if (not policy):
    print('please provide policy')
    return

  aws_s3_client.put_bucket_policy(Bucket=bucket_name, Policy=policy)
  print("Bucket multiple policy assigned successfully")