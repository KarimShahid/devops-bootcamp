# AWS CLI Setup

## Task

![Screenshot 2025-12-09 at 6.04.30 PM.png](images/Screenshot_2025-12-09_at_6.04.30_PM.png)

Install aws cli on MacOS 🍎

```bash
brew install awscli
```

check version

```bash
aws --version
```

Configure the cli

```bash
aws configure
```

![Screenshot 2025-12-09 at 6.03.09 PM.png](images/Screenshot_2025-12-09_at_6.03.09_PM.png)

## Creating a bucket via clickops

- Click on create a bucket

![Screenshot 2025-12-09 at 6.31.39 PM.png](images/Screenshot_2025-12-09_at_6.31.39_PM.png)

- The bucket name should be unique
- Keep everything default

![Screenshot 2025-12-09 at 6.32.59 PM.png](images/Screenshot_2025-12-09_at_6.32.59_PM.png)

- click on create bucket

![Screenshot 2025-12-09 at 6.34.04 PM.png](images/Screenshot_2025-12-09_at_6.34.04_PM.png)

Bucket is ready

![Screenshot 2025-12-09 at 6.34.40 PM.png](images/Screenshot_2025-12-09_at_6.34.40_PM.png)

Using CLI to check if bucket is available

```bash
aws s3 ls
```

![Screenshot 2025-12-09 at 6.35.20 PM.png](images/Screenshot_2025-12-09_at_6.35.20_PM.png)

## Creating a s3 bucket using CLI

```bash
aws s3 mb s3://<bucket-name> --region <region_name>

aws s3 mb s3://unique-bucket-9990 --region us-east-1
```

![Screenshot 2025-12-09 at 6.52.17 PM.png](images/Screenshot_2025-12-09_at_6.52.17_PM.png)

Copying files into s3

```bash
aws s3 cp <file-name> s3://<bucket_name> 

aws s3 cp <directory-name> s3://<bucket_name> --recursive
```

![Screenshot 2025-12-09 at 7.04.22 PM.png](images/Screenshot_2025-12-09_at_7.04.22_PM.png)

Checking inside the bucket

```bash
aws s3 ls s3://<bucket_name>/

# Lists all the dirs and files inside the bucket
aws s3 ls s3://<bucket_name>/ --recursive
```

![Screenshot 2025-12-09 at 7.09.55 PM.png](images/Screenshot_2025-12-09_at_7.09.55_PM.png)

Remember to use “/” to see the contents of a dir

![Screenshot 2025-12-09 at 7.10.43 PM.png](images/Screenshot_2025-12-09_at_7.10.43_PM.png)

## Hardening Tactics

1. DO NOT store credentials inside your project folders → Instead, AWS credentials must only live in 

~/.aws/credentials
~/.aws/config

1. Only your user should be able to read them.

![Screenshot 2025-12-09 at 7.40.12 PM.png](images/Screenshot_2025-12-09_at_7.40.12_PM.png)

2. Only your user should be able to read them. (Principle of Least Priviledge)
3. Rotate your Access Keys every 60–90 days
4. DO NOT export credentials in shell environment
5. Use AWS generated short term temporary credentials e.g via STS or Instance Role, instead of creating long term Access Keys for IAM users
6. Disabled/Delete unused Access Keys
7. Enable Two-factor authentication on IAM users