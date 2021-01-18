import boto3
from botocore.exceptions import ClientError

if __name__ == "__main__":
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()

        # Output the bucket names
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
    except ClientError as e:
        print(e)

    return True

