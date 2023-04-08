
import logging

import magic

ALLOWED_MIME_TYPES = ['image/bmp', 'image/jpeg', 'image/png', 'image/webp', 'video/mp4']

def download_file_and_upload_to_s3(aws_s3_client, bucket_name, url, file_name, keep_local=False):
    from urllib.request import urlopen
    import io
    
    with urlopen(url) as response:
        content = response.read()
        mime_type = magic.from_buffer(content, mime=True)
        if mime_type not in ALLOWED_MIME_TYPES:
            logging.error(f"Unsupported MIME type '{mime_type}'")
            return
        
        try:
            aws_s3_client.upload_fileobj(
                Fileobj=io.BytesIO(content),
                Bucket=bucket_name,
                ExtraArgs={'ContentType': mime_type},
                Key=file_name
            )
        except Exception as e:
            logging.error(e)
 
    if keep_local:
        with open(file_name, mode='wb') as file:
            file.write(content)
 
    return f"https://{aws_s3_client.meta.region_name}.amazonaws.com/{bucket_name}/{file_name}"###
