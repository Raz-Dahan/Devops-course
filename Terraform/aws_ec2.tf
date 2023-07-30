provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "test" {
  ami           = "ami-0e00e602389e469a3"
  instance_type = "t2.micro"

  tags = {
    Name = "TerraformTest"
  }
}
