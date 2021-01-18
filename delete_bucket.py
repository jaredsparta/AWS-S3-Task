import boto3
from botocore.exceptions import ClientError

def delete_a_bucket(bucket_name):
    try:
        s3 = boto3.client("s3")
        response = s3.delete_bucket()
    except ClientError as e:
        print(e)
        return False
    
    return print(response)

if __name__=="__main__":
    pass
