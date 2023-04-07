import boto3

def multipart_upload(file_path, bucket_name, object_key, chunk_size=1024 * 1024 * 5):
   
    s3 = boto3.client('s3')

    response = s3.create_multipart_upload(Bucket=bucket_name, Key=object_key)

    upload_id = response['UploadId']
    parts = []
    offset = 0
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            part = s3.upload_part(Body=data, Bucket=bucket_name, Key=object_key, PartNumber=len(parts) + 1, UploadId=upload_id)
            parts.append({'PartNumber': len(parts) + 1, 'ETag': part['ETag']})
            offset += len(data)

    s3.complete_multipart_upload(Bucket=bucket_name, Key=object_key, UploadId=upload_id, MultipartUpload={'Parts': parts})

    object_url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}"
    return object_url
