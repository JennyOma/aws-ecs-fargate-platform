output "ecr_repository_url" {
  description = "Address used when pushing a Docker image to ECR"
  value       = aws_ecr_repository.api.repository_url
}
