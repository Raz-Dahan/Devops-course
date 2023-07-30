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
}

resource "aws_instance" "test" {
  ami           = "ami-0e00e602389e469a3"
  instance_type = "t2.micro"

  tags = {
    Name = "TerraformTest"
  }

  key_name               = aws_key_pair.keypair.key_name
  vpc_security_group_ids = [aws_security_group.security_group.id]
}

resource "local_file" "public_ips" {
  filename = "public_ips.txt"
  content  = <<EOT
Instance Public IP: ${aws_instance.test.public_ip}
EOT
}
