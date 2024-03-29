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
  filename        = "tf-keypair.pem"
  content         = tls_private_key.keypair.private_key_pem
  file_permission = "0600"
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
  ami                    = "ami-0e00e602389e469a3"
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.keypair.key_name
  vpc_security_group_ids = [aws_security_group.security_group.id]

  tags = {
    Name     = "NASA App"
    platfrom = "flask"
    tier     = "production"
  }

  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = tls_private_key.keypair.private_key_pem
    host        = self.public_ip
  }

  provisioner "file" {
    source      = "docker-compose.yml"
    destination = "/home/ec2-user/docker-compose.yml"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install docker -y",
      "sudo systemctl enable docker.service",
      "sudo systemctl start docker.service",
      "sudo curl -L \"https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose",
      "sudo chmod +x /usr/local/bin/docker-compose",
      "sudo docker-compose -f /home/ec2-user/docker-compose.yml up -d",
    ]
  }
}

resource "local_file" "public_ips" {
  filename = "public_ips.txt"
  content  = <<EOT
Instance Public IP: ${aws_instance.app.public_ip}
EOT
}
