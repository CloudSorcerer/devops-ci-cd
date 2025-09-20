module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = var.cluster_name
  cluster_version = "1.28"
  subnets         = ["subnet-123", "subnet-456"] # replace with real
  vpc_id          = "vpc-123"                    # replace with real
}

output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}
