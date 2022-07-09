from logging import log
import boto3
import uuid
from tempfile import SpooledTemporaryFile

class AWSClient():
    def __init__(self) -> None:
        try:
            self.s3_client = boto3.client('s3')
            self.s3_resource = boto3.resource('s3')

        except Exception as e:
            print(e)

    def get_file_names(self, bucket_name: str) -> list:
        try:
            bucket = self.s3_resource.Bucket(name=bucket_name)
            file_name_list = []
            for obj in bucket.objects.all():
                file_name_list.append(obj.key)

            return file_name_list

        except Exception as e:
            print(e)
    
    def upload_file(self, bucket_name: str, file_name: str, key: str) -> None:
        try:
            self.s3_resource.Object(bucket_name,
                                    key).upload_file(Filename=file_name, ExtraArgs={'ACL': 'public-read'})

        except Exception as e:
            print(e)
            raise Exception