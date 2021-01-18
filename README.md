# S3 Task

![](images/cli-task.jpg)

<br>

### AWS S3 terminology
- `Key` - refers to the name you assign to an object
- `Value` - refers to the content you are storing
- `Metadata` - refers to a set of name-value pairs which stores information on the object

<br>

- Reference: [https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html)

<br>

### EC2 instance
- Create the EC2 instance on AWS
    - I used Ubuntu 18.04 as the AMI

<br>

### Installing AWSCLI
- When inside the EC2 instance, we will install the necessary dependencies:
    1. `sudo apt-get update`
    2. `sudo apt-get install python3-pip`
    3. `sudo apt-get install python3-venv`

- Create a virtual environment using `python3 -m venv <name>`

- Activate the virtual environment using `source <name>/bin/activate`
    - Within the `venv`, we will need to install `boto3`
    - Do this by running `pip3 install boto3`

- We now need to install `AWS CLI`. Follow the instructions found [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html) :
    1. `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`
    2. `sudo apt-get install unzip`
        - You will need this as unzip is not pre-installed with 18.04
    3. `unzip awscliv2.zip`
    4. `sudo ./aws/install`
    5. One can check the installation is complete via `aws --version`

- Now to configure the AWS settings, run `aws configure`
    - Input the access and secret keys when prompted
    - Select the default region (`eu-west-1` for Ireland)
    - Select a default output format (can use `json`)

<br>

### Using AWSCLI
- Check the docs to know how to write commands [here](https://docs.aws.amazon.com/cli/latest/index.html)


<br>

### Checking all available buckets in S3
- A simple script to check all available buckets is found in `check.py`
    - This can also be done through AWSCLI with `aws s3 ls`

```python
import boto3

if __name__ == "__main__":
    s3 = boto3.resource("s3")

    for bucket in s3.buckets.all():
        print(bucket.name)
```

<br>

### Creating an S3 bucket
- We first need to create a `client` for the `s3` service. This lets us do what we need to do
    - Creating an s3 client is as simple as assigning a variable with `boto3.client("s3")`
    - For instance `client = boto3.client("s3")`

- To create a bucket there is a method within `client` that lets us do so:
    - `boto3.client("s3").create_bucket(**kwargs)`

<br>

### Uploading a file onto S3
- There is also a built-in method for the `client` class that lets us upload files onto S3:
    - `boto3.client("s3").upload_file(<file_name>, <bucket>, <object_name>)`

<br>

### Retrieving a file from S3
- There are two similarly-named functions that achieve similar things: `download_file` vs. `download_fileobj`. What's the difference?
    - `download_file` downloads an S3 object to a file
    - `download_fileobj` downloads an S3 object to a file-like object. The object to download to must be in binary mode.

<br>

### Delete content from S3
- Again, we can use a built-in method called `delete_object()`
    - The entire line would be `boto3.client("s3").delete_object(<bucket_name>, <key>)`

<br>

### Deleting a bucket from S3
- `boto3.client("s3").delete_bucket()` requires all objects within the bucket to be removed before the bucket itself is. So what's the best way to remove all objects within a bucket?
    - Using the AWS CLI one can run the command `aws s3 rm s3://<bucket_name> --recursive` 

<br>

---
### Used:
- [AWS CLI](https://cloudacademy.com/blog/how-to-use-aws-cli/)
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
- [Resource vs. client vs. session](https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session)