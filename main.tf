provider "aws" {
    region = "eu-west-1"
}

resource "aws_security_group" "SG" {
    name = "eng74.jared.SG.docker.app"
    description = "SG for the app running in a docker container"

    ingress {
        description = "port 22 from home"
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = [var.personal_ip]
    }

    egress {
        description = "outbound with no restrictions"
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_instance" "instance" {
    ami = "ami-0dc8d444ee2a42d8a"
    instance_type = "t2.micro"
    associate_public_ip_address = true
    key_name = var.personal_key
    vpc_security_group_ids = [aws_security_group.SG.id]
    tags = {
      "Name" = "eng74-jared-s3-task"
    }
}