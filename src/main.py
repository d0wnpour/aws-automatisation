import argparse
import logging
from botocore.exceptions import ClientError
from init import init_client
from Bucket.list_bucket import list_buckets
from Bucket.create_bucket import create_bucket
from Bucket.delete_bucket import delete_bucket
from Bucket.bucket_exist import bucket_exists
from Bucket.Policy.multiple_policy import multiple_policy
from Bucket.Policy.asign_policy import assign_policy
from Bucket.Policy.public_read_policy import public_read_policy
from Bucket.Policy.read_bucket_policy import read_bucket_policy
#from Object.download_file_and_upload_to_s3 import download_file_and_upload_to_s3
from Object.set_object_access_policy import set_object_access_policy
from Object.multipart_upload import multipart_upload
from Object.upload_file import upload_file
from Object.upload_file_obj import upload_file_obj
from Object.upload_file_put import upload_file_put
from Object.add_lifecycle_policy import add_lifecycle_policy
from Object.delete_object import delete_object

parser = argparse.ArgumentParser(
   description="CLI S3 Bucket Helper"
)


parser.add_argument(
 "-lb",
  "--list_buckets",
  action="store_true",
  help="Users Bucket list",
)

parser.add_argument(
   "-cb",
   "--create_bucket",
   help="Create new bucket"
)

parser.add_argument(
   "-db",
   "--delete_bucket",
   help="Delete Existing Bucket"
)

parser.add_argument(
   "-be",
   "--bucket_exist",
   help="Returns Boolean depending on Bucket existence"
)

parser.add_argument(
    "-dl",
    "--download_and_upload",
    nargs=3, 
    metavar=("BUCKET_NAME", "URL", "FILE_NAME"),
    help="Download a file from URL and upload it to S3"
)

parser.add_argument(
    "-rbp",
    "--read_bucket_policy",
    help="Read policy of Existing Bucket"
)

parser.add_argument(
    "-prp",
    "--public_read_policy",
    help="Assign Public read policy to the Existing Bucket"
)

parser.add_argument(
    "-mp",
    "--multiple_policy",
    help="Assign Multiple policy to the Existing Bucket"
)

parser.add_argument(
    "-soap",
    "--set_object_access_policy",
    nargs=2,
    metavar=("BUCKET_NAME", "FILE_NAME"),
    help="Set access policy for an object in S3 bucket",
)

parser.add_argument(
        '-ulp',
        '--upload_large_file',
        nargs=3,
        metavar=('FILE_PATH', 'BUCKET_NAME', 'OBJECT_KEY'),
        help='Upload a large file to S3 using multipart upload.'
    )

parser.add_argument(
        "-uf",
        "--upload_file",
        nargs=2,
        metavar=("FILE_PATH", "BUCKET_NAME"),
        help="Upload a file to S3 bucket"
    )
parser.add_argument(
        "-ufo",
        "--upload_file_obj",
        nargs=3,
        metavar=("BUCKET_NAME", "FILE_NAME", "FILE_OBJ"),
        help="Upload a file object to S3 bucket with specific object name"
    )
parser.add_argument(
        "-ufp",
        "--upload_file_put",
        nargs=3,
        metavar=("FILE_PATH", "BUCKET_NAME", "FILE_NAME"),
        help="Upload a file to S3 bucket using the put method"
    )

parser.add_argument(
    "-alp", 
    "--add_lifecycle_policy", 
    nargs=3, 
    metavar=("BUCKET_NAME", "FILE_PREFIX", "EXPIRATION_DAYS"), 
    help="Add a lifecycle policy to an S3 bucket for a given file prefix with specified expiration period (in days)"
    
)

parser.add_argument(
    "-del",
    "--delete_object", 
    nargs=2, 
    metavar=("OBJECT_NAME", "BUCKET_NAME"), 
    help="Delete an object from S3 bucket"    
)

def main():
    s3_client = init_client()
    args = parser.parse_args()

    if (args.list_buckets):
        buckets = list_buckets(s3_client)
        if buckets:
            for bucket in buckets['Buckets']:
                print(f'  {bucket["Name"]}')

    if args.create_bucket:
        bucket_name = args.create_bucket
        try:
            s3_client.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' created successfully!")
        except ClientError as e:
            logging.error(e)

    if args.delete_bucket:
        bucket_name = args.delete_bucket
        try:
            delete_bucket(s3_client, bucket_name)
            print(f"Bucket '{bucket_name}' deleted successfully!")
        except ClientError as e:
            logging.error(e)
    
    if args.bucket_exist:
        bucket_name = args.bucket_exist
        exists = bucket_exists(s3_client, bucket_name)
        if exists:
            print(f"Bucket '{bucket_name}' exists!")
        else:
            print(f"Bucket '{bucket_name}' does not exist.")

    #if args.download_and_upload:
        #bucket_name, url, file_name = args.download_and_upload
        #download_file_and_upload_to_s3(s3_client, bucket_name, url, file_name, keep_local=False)

    if args.read_bucket_policy:
        bucket_name = args.read_bucket_policy
        policy = read_bucket_policy(s3_client, bucket_name)
        if policy:
            print(f"Bucket policy: {policy}")
        else:
            print(f"No policy found for Bucket '{bucket_name}'")

    if args.public_read_policy:
        bucket_name = args.public_read_policy
        assign_policy(s3_client, "public_read_policy", bucket_name)

    if args.multiple_policy:
        bucket_name = args.multiple_policy
        assign_policy(s3_client, "multiple_policy", bucket_name)

    if args.set_object_access_policy:
        bucket_name, file_name, = args.set_object_access_policy
        if set_object_access_policy(s3_client, bucket_name, file_name):
            print(f"Access policy for object '{file_name}' in bucket '{bucket_name}' set successfully!")
        else:
            print(f"Failed to set access policy for object '{file_name}' in bucket '{bucket_name}'.")

    if args.upload_file:
        file_path, bucket_name = args.upload_file
        try:
            s3_client.upload_file(file_path, bucket_name, file_path.split("/")[-1])
            print(f"File '{file_path}' uploaded to '{bucket_name}' successfully!")
        except ClientError as e:
            logging.error(e)
    
    
    if args.upload_large_file:
        file_path, bucket_name, object_key = args.upload_large_file
        object_url = multipart_upload(file_path, bucket_name, object_key)
        print(f'Object uploaded successfully. URL: {object_url}')

    if args.upload_file_obj:
        bucket_name, file_name, file_path = args.upload_file_obj
        try:
            with open(file_path, 'rb') as f:
                s3_client.upload_fileobj(f, bucket_name, file_name)
            print(f"File '{file_name}' uploaded to bucket '{bucket_name}' successfully!")
        except ClientError as e:
            logging.error(e)

    if args.upload_file_put:
        file_path, bucket_name, file_name = args.upload_file_put
        try:
            with open(file_path, "rb") as file:
                s3_client.put_object(Body=file, Bucket=bucket_name, Key=file_name)
            print(f"File '{file_name}' uploaded to bucket '{bucket_name}' successfully!")
        except ClientError as e:
            logging.error(e)
    if args.add_lifecycle_policy:
        add_lifecycle_policy(args.add_lifecycle_policy[0], args.add_lifecycle_policy[1], int(args.add_lifecycle_policy[2]))

    if args.delete_object is not None:
        delete_object(args.delete_object[0], args.delete_object[1])
    

    
if __name__ == "__main__":
  try:
    main()
  except ClientError as e:
    logging.error(e)