
# EBS volumes
data "aws_ebs_volume" "gp2_volume" {
  most_recent = true

  filter {
    name   = "volume-type"
    values = ["gp2"]
  }
}


data "aws_s3_bucket" "selected" {
  bucket = "bucket.test.com"
}

# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/s3_bucket