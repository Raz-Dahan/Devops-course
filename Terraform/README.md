# Terraform AWS Infrastructure

This repository contains Terraform configuration files to provision AWS resources. The infrastructure includes three Terraform files that can be activated by following the instructions below.

## Prerequisites

Before using these Terraform files, ensure you have the following prerequisites:

1. [Terraform](https://www.terraform.io/downloads.html) installed on your local machine.
2. An AWS account with appropriate access and IAM credentials configured.

## Getting Started

Follow these steps to deploy the AWS infrastructure using Terraform:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/terraform-aws-infrastructure.git
cd terraform-aws-infrastructure
```

2. Initialize Terraform within each sub-folder containing the Terraform files.

```bash
cd path/to/tf-file1
terraform init

cd path/to/tf-file2
terraform init

cd path/to/tf-file3
terraform init
```

3. Review the Terraform plans to understand the changes that will be made to your AWS account.

```bash
cd path/to/tf-file1
terraform plan

cd path/to/tf-file2
terraform plan

cd path/to/tf-file3
terraform plan
```

4. If the Terraform plans look good, proceed with applying them.

```bash
cd path/to/tf-file1
terraform apply

cd path/to/tf-file2
terraform apply

cd path/to/tf-file3
terraform apply
```

## SSH Key for Instances

Two of the Terraform configurations create instances and also generate an RSA key for each instance. To connect to these instances via SSH, follow these steps:

1. After applying the Terraform configuration, you will find the generated RSA private key files (`*.pem`) in the respective Terraform folders.

2. Move the private key file (`*.pem`) to your desired location.

3. Secure the private key file with appropriate permissions.

```bash
chmod 400 /path/to/your/private-key.pem
```

4. Connect to the instance using SSH and the private key file.

```bash
ssh -i "/path/to/your/private-key.pem" ec2-user@instance-ip-address
```

## Public IPs

Two of the Terraform configurations generate an output file named `public-ips.txt`, which contains the public IP addresses of the created instances. You can find this file in the respective Terraform folders after applying the configuration.

### Caution

- **Warning**: These Terraform configurations will create AWS resources that may incur costs in your AWS account. Make sure to review the Terraform plans before applying them.
- **Clean Up**: To avoid unexpected charges, don't forget to destroy the resources when they are no longer needed, using `terraform destroy` within each respective Terraform folder.

If you have any questions or issues, feel free to create an issue in this repository or contact the repository owner. Happy Terraforming! 🚀