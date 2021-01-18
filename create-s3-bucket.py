import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name="eng74-jared-bucket-boto3", region="eu-west-1"):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            response = s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
                                    
    except ClientError as e:
        print(e)
        return False
        
    return print(response)

if __name__ == "__main__":
    pass
