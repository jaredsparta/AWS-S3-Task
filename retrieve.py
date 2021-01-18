import boto3
from botocore.exceptions import ClientError

def download_a_file(bucket_name, object_name, file_name):
    try:
        s3 = boto3.client('s3')
        s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
    except ClientError as e:
        print(e)
        return False
    return True

if __name__ == "__main__":
    pass