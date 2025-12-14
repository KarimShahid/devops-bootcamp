# EC2 creation via IAC → CloudFormation

![Screenshot 2025-12-14 at 2.54.17 PM.png](images/Screenshot_2025-12-14_at_2.54.17_PM.png)

Creating a cloudformation template

ec2-cft.yaml

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: CloudFormation template to create EC2 instance with EIP.

Parameters:
  SubnetId:
    Type: AWS::EC2::Subnet::Id
    Description: Select a subnet in the chosen VPC

  SecurityGroupId:
    Type: AWS::EC2::SecurityGroup::Id
    Description: Select an existing Security Group

  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instance
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: must be the name of an existing EC2 KeyPair.

  InstanceType:
    Description: WebServer EC2 instance type
    Type: String
    AllowedValues:
      - t3.micro
      - t3.small
    Default: t3.micro
    ConstraintDescription: must be a valid EC2 instance type.

Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-068c0051b15cdb816   # Amazon Linux
      InstanceType: !Ref InstanceType
      KeyName: !Ref KeyName
      SubnetId: !Ref SubnetId
      SecurityGroupIds: 
      - !Ref SecurityGroupId 
      #Advanced Tab
      CreditSpecification:
        CPUCredits: standard      
      Tags:
      - Key: Name
        Value: Karim-EC2
      - Key: ManagedBy
        Value: CloudFormation 

  ElasticIP:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc
      Tags:
        - Key: Name
          Value: Karim-ElasticIP

  EIPAssociation:
    Type: AWS::EC2::EIPAssociation
    Properties:
      InstanceId: !Ref EC2Instance
      EIP: !Ref ElasticIP
  
Outputs:
  InstanceId:
    Description: InstanceId of the newly created EC2 instance
    Value: !Ref EC2Instance

  AZ:
    Description: Availability Zone of the newly created EC2 instance
    Value: !GetAtt EC2Instance.AvailabilityZone

  PublicDNS:
    Description: Public DNSName of the newly created EC2 instance
    Value: !GetAtt EC2Instance.PublicDnsName

  PublicIP:
    Description: Public IP address of the newly created EC2 instance. (Elastic IP)
    Value: !GetAtt EC2Instance.PublicIp
```

## Uploading to cloudFormation via console

![Screenshot 2025-12-14 at 2.26.06 PM.png](images/Screenshot_2025-12-14_at_2.26.06_PM.png)

Add the required .yaml file

![Screenshot 2025-12-14 at 2.27.05 PM.png](images/Screenshot_2025-12-14_at_2.27.05_PM.png)

View in Infrastructure Composer and validate the template

Keep in mind that Infrastructure doesnt like Description in resources.

![Screenshot 2025-12-14 at 2.31.12 PM.png](images/Screenshot_2025-12-14_at_2.31.12_PM.png)

Select the required Parameters

![Screenshot 2025-12-14 at 2.38.20 PM.png](images/Screenshot_2025-12-14_at_2.38.20_PM.png)

Keep things default

![Screenshot 2025-12-14 at 2.39.13 PM.png](images/Screenshot_2025-12-14_at_2.39.13_PM.png)

Stack Created Sucessfully.

![Screenshot 2025-12-14 at 2.41.04 PM.png](images/Screenshot_2025-12-14_at_2.41.04_PM.png)

Resources Created

![Screenshot 2025-12-14 at 2.41.36 PM.png](images/Screenshot_2025-12-14_at_2.41.36_PM.png)

Updating the Stack

Select the stack → Update Stack → Create Change set

![Screenshot 2025-12-14 at 2.44.56 PM.png](images/Screenshot_2025-12-14_at_2.44.56_PM.png)

Edit in Composer

![Screenshot 2025-12-14 at 2.47.20 PM.png](images/Screenshot_2025-12-14_at_2.47.20_PM.png)

Make small update

Update the tag “Karim-EC2” → “Updated-Karim-EC2”

Save → Create Change Set

![Screenshot 2025-12-14 at 2.48.17 PM.png](images/Screenshot_2025-12-14_at_2.48.17_PM.png)

![Screenshot 2025-12-14 at 2.49.51 PM.png](images/Screenshot_2025-12-14_at_2.49.51_PM.png)

![Screenshot 2025-12-14 at 2.50.21 PM.png](images/Screenshot_2025-12-14_at_2.50.21_PM.png)

Change Set Details

![Screenshot 2025-12-14 at 2.52.18 PM.png](images/Screenshot_2025-12-14_at_2.52.18_PM.png)

Review

![Screenshot 2025-12-14 at 2.52.33 PM.png](images/Screenshot_2025-12-14_at_2.52.33_PM.png)

Execute Change Set

![Screenshot 2025-12-14 at 2.53.00 PM.png](images/Screenshot_2025-12-14_at_2.53.00_PM.png)

Update Complete

![Screenshot 2025-12-14 at 2.56.39 PM.png](images/Screenshot_2025-12-14_at_2.56.39_PM.png)

Tags are changed

![Screenshot 2025-12-14 at 2.57.23 PM.png](images/Screenshot_2025-12-14_at_2.57.23_PM.png)

Delete the stack/resources

Click “Delete”

![Screenshot 2025-12-14 at 2.58.54 PM.png](images/Screenshot_2025-12-14_at_2.58.54_PM.png)

![Screenshot 2025-12-14 at 2.59.22 PM.png](images/Screenshot_2025-12-14_at_2.59.22_PM.png)

![Screenshot 2025-12-14 at 3.00.01 PM.png](images/Screenshot_2025-12-14_at_3.00.01_PM.png)

# Using AWS - CLI

Add UserData to ec2-cft.yaml

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: CloudFormation template to create EC2 instance with EIP.

Parameters:
  SubnetId:
    Type: AWS::EC2::Subnet::Id
    Description: Select a subnet in the chosen VPC

  SecurityGroupId:
    Type: AWS::EC2::SecurityGroup::Id
    Description: Select an existing Security Group

  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instance
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: must be the name of an existing EC2 KeyPair.

  InstanceType:
    Description: WebServer EC2 instance type
    Type: String
    AllowedValues:
      - t3.micro
      - t3.small
    Default: t3.micro
    ConstraintDescription: must be a valid EC2 instance type.

Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-068c0051b15cdb816   # Amazon Linux
      InstanceType: !Ref InstanceType
      KeyName: !Ref KeyName
      SubnetId: !Ref SubnetId
      SecurityGroupIds: 
      - !Ref SecurityGroupId 
      #Advanced Tab
      CreditSpecification:
        CPUCredits: standard      
      Tags:
      - Key: Name
        Value: Karim-EC2
      - Key: ManagedBy
        Value: CloudFormation 
      UserData:    # must be exactly 'UserData'
        Fn::Base64: |
          #!/bin/bash
          dnf update -y 
          dnf install -y nginx
          systemctl enable nginx
          systemctl start nginx
          echo "Hello World" > /usr/share/nginx/html/index.html

  ElasticIP:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc
      Tags:
        - Key: Name
          Value: Karim-ElasticIP

  EIPAssociation:
    Type: AWS::EC2::EIPAssociation
    Properties:
      InstanceId: !Ref EC2Instance
      EIP: !Ref ElasticIP
  
Outputs:
  InstanceId:
    Description: InstanceId of the newly created EC2 instance
    Value: !Ref EC2Instance

  AZ:
    Description: Availability Zone of the newly created EC2 instance
    Value: !GetAtt EC2Instance.AvailabilityZone

  PublicDNS:
    Description: Public DNSName of the newly created EC2 instance
    Value: !GetAtt EC2Instance.PublicDnsName

  PublicIP:
    Description: Public IP address of the newly created EC2 instance. (Elastic IP)
    Value: !GetAtt EC2Instance.PublicIp
```

Make sure that aws configure has the proper credentials

![Screenshot 2025-12-14 at 7.03.36 PM.png](images/Screenshot_2025-12-14_at_7.03.36_PM.png)

Make sure that template is valid 

```bash
aws cloudformation create-stack --stack-name MyStack --template-body file://ec2-cft.yaml
```

![Screenshot 2025-12-14 at 6.39.17 PM.png](images/Screenshot_2025-12-14_at_6.39.17_PM.png)

Create the stack using the template

```bash
aws cloudformation create-stack \
  --stack-name MyEC2Stack \
  --template-body file://~/Documents/AWS-adex/ec2-cft.yaml \
  --parameters \
      ParameterKey=KeyName,ParameterValue=awsKeyPair \
      ParameterKey=SubnetId,ParameterValue=subnet-0fd893a7a2e4249b5 \
      ParameterKey=SecurityGroupId,ParameterValue=sg-05dbbd278e09a6b2b \
      ParameterKey=InstanceType,ParameterValue=t3.micro
```

![Screenshot 2025-12-14 at 7.00.02 PM.png](images/Screenshot_2025-12-14_at_7.00.02_PM.png)

Check Status

```bash
aws cloudformation describe-stacks --stack-name Karim-EC2Stack --query "Stacks[0].StackStatus"
```

![Screenshot 2025-12-14 at 7.00.13 PM.png](images/Screenshot_2025-12-14_at_7.00.13_PM.png)

![Screenshot 2025-12-14 at 7.00.36 PM.png](images/Screenshot_2025-12-14_at_7.00.36_PM.png)

![Screenshot 2025-12-14 at 7.00.53 PM.png](images/Screenshot_2025-12-14_at_7.00.53_PM.png)

Outputs

```bash
aws cloudformation describe-stacks --stack-name MyEC2Stack --query "Stacks[0].Outputs"
```

![Screenshot 2025-12-14 at 7.01.49 PM.png](images/Screenshot_2025-12-14_at_7.01.49_PM.png)

Using the EIP to access the web-site

![Screenshot 2025-12-14 at 7.02.18 PM.png](images/Screenshot_2025-12-14_at_7.02.18_PM.png)