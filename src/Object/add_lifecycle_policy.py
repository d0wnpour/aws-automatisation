import boto3

def add_lifecycle_policy(bucket_name, file_prefix, expiration_days):
    lifecycle_policy = {
        "Rules": [
            {
                "ID": "delete_after_{}days".format(expiration_days),
                "Prefix": file_prefix,
                "Status": "Enabled",
                "Expiration": {"Days": expiration_days},
            }
        ]
    }
    s3 = boto3.client("s3")
    s3.put_bucket_lifecycle_configuration(Bucket=bucket_name, LifecycleConfiguration=lifecycle_policy)
    print("Lifecycle policy added to bucket '{}' for file prefix '{}' with expiration of {} days".format(bucket_name, file_prefix, expiration_days))
