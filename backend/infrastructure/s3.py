import boto3

def create_s3_client(aws_access_key, aws_secret_key, region):
    return boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )