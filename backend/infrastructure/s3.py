import boto3
from botocore.config import Config

class MallS3:
    def __init__(self,aws_access_key, aws_secret_key, region,bucket):
        self.bucket = bucket
        self.s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region,
        config=Config(signature_version='s3v4'),
        endpoint_url=f'https://s3.{region}.amazonaws.com')


    def generate_presigned_url(self, key):
        url = self.s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': self.bucket,
            'Key': key,
        },
        ExpiresIn=3600
    )
        return url
    
    def upload_file(self,file_data,key,content_type):
        self.s3_client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=file_data,
            ContentType=content_type
        )