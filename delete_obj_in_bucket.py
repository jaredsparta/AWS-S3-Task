import boto3
from botocore.exceptions import ClientError

def remove_obj_bucket(bucket_name, key):
    try:
        s3 = boto3.client("s3")
        response = s3.delete_object(bucket_name, key)
    except ClientError as e:
        print(e)
        return False
    
    return print(response)

if __name__ == "__main__":
    pass
