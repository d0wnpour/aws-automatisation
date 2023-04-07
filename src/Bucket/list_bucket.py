import logging
from botocore.exceptions import ClientError

def list_buckets(aws_s3_client):
    try:
        return aws_s3_client.list_buckets()
    except ClientError as e:
        logging.error(e)
        return False