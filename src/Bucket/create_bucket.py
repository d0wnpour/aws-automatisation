from os import getenv
import logging
from botocore.exceptions import ClientError

def create_bucket(aws_s3_client, bucket_name, region=getenv("aws_region_name")):
    try:
        location = {'LocationConstraint': region}
        response = aws_s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration=location
        )
    except ClientError as e:
        logging.error(e)
        return False
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code == 200:
        return True
    return False