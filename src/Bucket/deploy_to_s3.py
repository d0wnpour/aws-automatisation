import json
import os
import mimetypes

def deploy_to_s3(s3_client, bucket_name, source_path):
    # Create a new website configuration
    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'}
    }

    # Set the website configuration for the bucket
    s3_client.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration=website_configuration
    )

    # Set the bucket policy to allow public read access
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": [
                    f"arn:aws:s3:::{bucket_name}/*"
                ]
            }
        ]
    }
    policy_json = json.dumps(policy)
    s3_client.put_bucket_policy(Bucket=bucket_name, Policy=policy_json)

    # List of excluded file and directory names
    excluded_names = ['.git']

    # Upload files from source to S3 bucket
    for dirpath, dirnames, filenames in os.walk(source_path):
        # Exclude any directories or files that start with a dot or are in the excluded_names list
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in excluded_names]
        filenames = [f for f in filenames if not f.startswith('.') and f not in excluded_names]

        for filename in filenames:
            local_file_path = os.path.join(dirpath, filename)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                s3_file_path = 'images/' + local_file_path.replace(source_path, '', 1).lstrip(os.path.sep)
                s3_file_path = 'images/' + os.path.basename(s3_file_path)
            else:
                s3_file_path = local_file_path.replace(source_path, '', 1).lstrip(os.path.sep)

            content_type = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
            extra_args = {'ContentType': content_type}
            s3_client.upload_file(local_file_path, bucket_name, s3_file_path, ExtraArgs=extra_args)
    
    url = f'http://{bucket_name}.s3-website.{s3_client.meta.region_name}.amazonaws.com/index.html'
    return url       
