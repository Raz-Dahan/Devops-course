provider "aws" {
  region = "eu-central-1"
}

resource "tls_private_key" "keypair" {
  algorithm = "RSA"
}

resource "aws_key_pair" "keypair" {
  key_name   = "tf-keypair"
  public_key = tls_private_key.keypair.public_key_openssh
}

resource "local_file" "private_key" {
  filename = "tf-keypair.pem"
  content  = tls_private_key.keypair.private_key_pem
}

resource "aws_security_group" "security_group" {
  name_prefix = "tf-security-group"
  vpc_id      = "vpc-075cb68ba343c4d30"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "nginx" {
  ami           = "ami-0e00e602389e469a3"
  instance_type = "t2.micro"

  tags = {
    Name     = "Nginx"
    platfrom = "terraform"
  }

  key_name               = aws_key_pair.keypair.key_name
  vpc_security_group_ids = [aws_security_group.security_group.id]

  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install nginx -y
    systemctl start nginx
    systemctl enable nginx
    EOF
}

resource "local_file" "public_ips" {
  filename = "public_ips.txt"
  content  = <<EOT
Instance Public IP: ${aws_instance.nginx.public_ip}
EOT
}
