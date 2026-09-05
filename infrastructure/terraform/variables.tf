variable "aws_region" {
  description = "AWS region for JobFlow infrastructure"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for AWS resources"
  type        = string
  default     = "jobflow"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}