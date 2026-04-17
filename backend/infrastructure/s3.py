import boto3


class MallS3:
    def __init__(self,aws_access_key, aws_secret_key, region,bucket):
        self.bucket = bucket
        self.s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region)


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