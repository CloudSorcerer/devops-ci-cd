terraform {
  required_version = ">= 1.6.0"
  backend "s3" {
    bucket         = "ci-cd-demo-tfstate"
    key            = "terraform/state"
    region         = "us-east-1"
    dynamodb_table = "ci-cd-locks"
  }
}

provider "aws" {
  region = var.aws_region
}
