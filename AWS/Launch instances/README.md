# Launch Instances

This repository contains code to run instances for test purposes on AWS. Feel free to clone the repository and modify the JSON configuration file according to your needs.

## Prerequisites

Before running the code, please ensure that you have set up your AWS credentials by executing the following command and providing your AWS access key ID, secret access key, default region name, and output format:

```
aws configure
```

## Usage

To start the instances, use the following command:

```
aws ec2 run-instances --cli-input-json file://runinstances-config.json
```

Make sure to modify the `runinstances-config.json` file to specify the desired instance configuration, such as the AMI ID, instance type, security groups, and key pair.
