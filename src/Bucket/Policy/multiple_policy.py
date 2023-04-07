import json

def multiple_policy(bucket_name):
  policy = {
    "Version":
    "2012-10-17",
    "Statement": [{
      "Action": [
        "s3:PutObject", "s3:PutObjectAcl", "s3:GetObject", "s3:GetObjectAcl",
        "s3:DeleteObject"
      ],
      "Resource":
      [f"arn:aws:s3:::{bucket_name}", f"arn:aws:s3:::{bucket_name}/*"],
      "Effect":
      "Allow",
      "Principal":
      "*"
    }]
  }

  return json.dumps(policy)