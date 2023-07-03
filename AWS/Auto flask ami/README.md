Sure! Here's an organized version of the README:

## Auto Flask AMI Creation

This script helps you create an AWS AMI with an always running Flask app. The script is designed to run on AWS CloudShell, but it can also be executed on your local machine. Please ensure that you have the AWS CLI installed and perform the necessary AWS configuration. Additionally, make sure to update the path in the `run-instances` command to match your environment.

### Prerequisites

- AWS CLI installed
- AWS configured with your credentials

### Instructions

1. Clone this repository to your local machine or AWS CloudShell.
2. Open a terminal or AWS CloudShell.
3. Change into the cloned repository directory.

   ```bash
   cd Devops-course/AWS/Auto\ flask\ ami
   ```

4. Update the `run-instances` command in the `create_ami.sh` script with the correct path to your key pair and security group. This will ensure that your instances have the necessary access and security settings.

   ```bash
   aws ec2 run-instances --image-id <AMI_ID> --count 1 --instance-type <INSTANCE_TYPE> --key-name <KEY_PAIR_NAME> --security-group-ids <SECURITY_GROUP_ID> --user-data file://<your-current-path>/user_data.sh
   ```

5. Run the `create_ami.sh` script to create the AMI.

   ```bash
   ./create_ami.sh
   ```

6. The script will create an EC2 instance with the specified AMI ID and instance type. It will execute the `bootstrap.sh` script, which installs all necessary dependencies, sets up the Flask app, and starts the server.

7. Once the script finishes executing, you will have an AMI with an always running Flask app.
