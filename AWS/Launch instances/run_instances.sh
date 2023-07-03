#!/bin/bash

echo'{
  "MaxCount": 2,
  "MinCount": 2,
  "ImageId": "ami-0b2ac948e23c57071",
  "InstanceType": "t2.micro",
  "KeyName": "raz-key",
  "EbsOptimized": false,
  "NetworkInterfaces": [
    {
      "AssociatePublicIpAddress": true,
      "DeviceIndex": 0,
      "Groups": [
        "sg-06fe143a3a8ada778"
      ]
    }
  ],
  "TagSpecifications": [
    {
      "ResourceType": "instance",
      "Tags": [
        {
          "Key": "Name",
          "Value": "Prod"
        },
        {
          "Key": "platform",
          "Value": "production"
        }
      ]
    }
  ],
  "IamInstanceProfile": {
    "Arn": "arn:aws:iam::820997886839:instance-profile/S3+EC2-Access"
  },
  "PrivateDnsNameOptions": {
    "HostnameType": "ip-name",
    "EnableResourceNameDnsARecord": true,
    "EnableResourceNameDnsAAAARecord": false
  }
}' > config.json

aws ec2 run-instances --cli-input-json file://config.json
