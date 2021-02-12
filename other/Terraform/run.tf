terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

// --- All local variables
variable "source_instance_id" {
  type        = string
  description = "The id of the instance to use for AMI creation."

  validation {
    condition     = length(var.source_instance_id) > 2 && substr(var.source_instance_id, 0, 2) == "i-"
    error_message = "The source_instance_id value must be a valid Instance id, starting with \"i-\"."
  }
}

variable "source_ami_name" {
  type        = string
  description = "The name of the AMI."
}

variable "ami_desc" {
  type        = string
  description = "The description for AMI."
}

variable "launch_template_name" {
  type        = string
  description = "The name of the launch template."
}

variable "launch_template_desc" {
  type        = string
  description = "The description of the launch template."
}

variable "lt_instance_type" {
  type        = string
  description = "The instance type for launch template."
}

variable "lt_key_name" {
  type        = string
  description = "The key (PEM) name for launch template."
}

variable "lt_security_groups" {
  type        = list(string)
  description = "The security groups for launch template."
  default     = ["sg-010e9e760a4b78e08"]
}

variable "lt_machine_name" {
  type        = string
  description = "Name for instance and volumes for launch template."
}

// --- Create AMI from an instance

resource "aws_ami_from_instance" "example" {
  name               = var.source_ami_name
  source_instance_id = var.source_instance_id

  lifecycle {
    prevent_destroy = true
  }
}


// --- Retrieve data on AWS AMI

data "aws_ami" "ami_data" {
  owners = ["self"]

  filter {
    name   = "name"
    values = [var.source_ami_name]
  }

  depends_on = [
    aws_ami_from_instance.example,
  ]
}

locals {
  ami_block_device_name = {
    for bd in data.aws_ami.ami_data.block_device_mappings :
    bd.device_name => bd
  }
}
output "ami_data_op" {
  value = aws_ami_from_instance.example
  depends_on = [
    aws_ami_from_instance.example
  ]
}


// --- Update an existing launch template
# data "aws_launch_template" "lt_data" {
#   name = var.launch_template_name
# }


resource "aws_launch_template" "tf_launch_template" {

  name        = var.launch_template_name
  description = var.launch_template_desc

  image_id      = data.aws_ami.ami_data.image_id
  instance_type = var.lt_instance_type
  key_name      = var.lt_key_name

  vpc_security_group_ids = var.lt_security_groups

  block_device_mappings {

    // Assumes device_name to be "/dev/sda1" for AMI
    // TODO: Add a check to stop running if /dev/sda1 is not found
    device_name = "/dev/sda1"

    ebs {
      delete_on_termination = true
      encrypted             = local.ami_block_device_name["/dev/sda1"].ebs.encrypted
      volume_size           = local.ami_block_device_name["/dev/sda1"].ebs.volume_size
      volume_type           = local.ami_block_device_name["/dev/sda1"].ebs.volume_type
      snapshot_id           = local.ami_block_device_name["/dev/sda1"].ebs.snapshot_id
    }
  }

  tag_specifications {
    resource_type = "instance"

    tags = {
      Machine-Category = var.lt_machine_name
    }
  }

  tag_specifications {
    resource_type = "volume"

    tags = {
      Machine-Category = var.lt_machine_name
    }
  }

  ebs_optimized = false
  credit_specification {
    cpu_credits = "unlimited"
  }

  update_default_version = true

  lifecycle {
    prevent_destroy = true
  }

  depends_on = [
    aws_ami_from_instance.example,
    data.aws_ami.ami_data
  ]
}


# --- Retrieve data on launch template
data "aws_launch_template" "lt_data" {
  name = var.launch_template_name
}

output "lt_op" {
  value = data.aws_launch_template.lt_data
}
