terraform {
  backend "s3" {
    bucket       = "dev-mandloi-eks-tfstate-ap-south-1"
    key          = "eks/terraform.tfstate"
    region       = "ap-south-1"
    encrypt      = true
    use_lockfile = true
  }
}
