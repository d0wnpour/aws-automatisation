# CLI tool for AWS S3



![Python](https://ibb.co/FXLPP90)

Tool was created for educational purposes. It will be updated time by time and new servises will be added.

#### To run this project you should have:
- Python 3
- Poetry

| Download Python 3 From: <br>
<a href="http://python.org/">``` http://www.python.org/ ```</a>

| install poetry <br>
```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -```

Or via PIP <br>
``` pip install poetry ```

to install project dependencies on local machine use command: <br>
```poetry install ```

<p align=center>Used Methodes:</p>

| Acts on | Name | Description | Flag |
|:---------------|:---------------|:---------------|:---------------|
| Bucket  | list_bucket | Displays existing buckets  | ``` -lb or --list_buckets```  |
| Bucket  | create_bucket  | Creates S3 Bucket  | ```-cb or --create_bucket```  |
| Bucket  | delete_bucket  | Deletes S3 Bucket  | ```-db or --delete_bucket```  |
| Bucket  |  bucket_exists | Checks Bucket Existence  | ```-be or --bucket_exist```  |
| Bucket  | public_read_policy  | Assign Public read policy to the Existing Bucket  | ```-prp or --public_read_policy``` |
| Bucket  | read_bucket_policy  | Read policy of Existing Bucket  | ```-rbp or --read_bucket_policy``` |
| Bucket  | multiple_policy  | Assing multiple policy to Existing Bucket  | ``` -mp or --multiple_policy```|
| Object  | download_file_and_upload_to_s3  | Downloads File and uploades it on S3 Bucket  | ``` -dl or --download_and_upload```  |
| Object  | set_object_access_policy  | Sets Access policy to object  | ```-soap or --set_object_access_policy``` |
| Object | multipart_upload | Uploades large files on bucket | ```-ulp or --upload_large_file``` |
| Object | upload_file | Uploades file to bucket | ```-uf or --upload_file``` |
| Object | upload_file_obj | Uploades file with object key | ```-ufo or --upload_file_ob``` |
| Object | upload_file_put | Uploades file with put method | ```-ufp or --upload_file_put``` |
| Object | add_lifecycle_policy | Deletes object after specified amount of time | ```-alp or --add_lifecycle_policy``` |
| Object | delete_object | Deletes given object from Bucket | ```-del or --delete_object``` |

## Used Tools:
- ```boto 3```
- ```python-magic```
- ```python-dotenv```
- ```argparse```




> Business And Technology University <br> 
> Author: <b>Rati Alania</b> <br>
> Lecturer: <b>Guja Nemsadze</b>
