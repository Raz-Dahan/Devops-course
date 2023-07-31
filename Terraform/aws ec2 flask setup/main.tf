provider "aws" {
  region = "eu-central-1"
}

resource "null_resource" "change_permissions" {
  triggers = {
    ssh_key_file = tls_private_key.keypair.private_key_pem
  }

  provisioner "local-exec" {
    command = "chmod 600 ${local_file.private_key.filename}"
  }
}
resource "tls_private_key" "keypair" {
  algorithm = "RSA"
}

resource "aws_key_pair" "keypair" {
  key_name   = "tf-keypair"
  public_key = tls_private_key.keypair.public_key_openssh

  lifecycle {
    ignore_changes = [key_name]
  }
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
    from_port   = 5000
    to_port     = 5000
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

resource "aws_instance" "app" {
  ami           = "ami-0e00e602389e469a3"
  instance_type = "t2.micro"

  tags = {
    Name     = "NASA App"
    platfrom = "flask"
    tier     = "production"
  }

  key_name               = aws_key_pair.keypair.key_name
  vpc_security_group_ids = [aws_security_group.security_group.id]

  provisioner "remote-exec" {
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = tls_private_key.keypair.private_key_pem
      host        = self.public_ip
    }

    inline = [
      "sudo yum update -y",
      "sudo yum install git -y",
      "git clone https://github.com/Raz-Dahan/Devops-course.git",
      "sudo yum install docker -y",
      "sudo systemctl enable docker.service",
      "sudo systemctl start docker.service",
      "sudo curl -L \"https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose",
      "sudo chmod +x /usr/local/bin/docker-compose",
      "sudo docker-compose -f Devops-course/Terraform/aws-ec2-flask-setup/docker-compose.yml up -d",
    ]
  }
}

resource "local_file" "public_ips" {
  filename = "public_ips.txt"
  content  = <<EOT
Instance Public IP: ${aws_instance.app.public_ip}
EOT
}
