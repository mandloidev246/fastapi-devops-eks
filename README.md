🚀 FastAPI DevOps Deployment on AWS EKS
📌 Overview

This project demonstrates an end-to-end DevOps workflow for deploying a production-ready FastAPI REST API on AWS EKS, focusing on automation, scalability, security, and cost awareness.

The application is containerized using Docker, infrastructure is provisioned with Terraform, Kubernetes resources are managed using Helm, and the entire pipeline is automated via GitHub Actions.

🏗️ Architecture Overview

Flow:

GitHub → GitHub Actions → Docker Hub → AWS EKS → Kubernetes (Helm)


Key Components:

FastAPI application

Dockerized container image

AWS infrastructure provisioned using Terraform

Kubernetes cluster on AWS EKS

Helm charts for application deployment

CI/CD pipeline using GitHub Actions

Remote Terraform backend using S3 + DynamoDB for state locking

🧰 Tech Stack

Backend: FastAPI (Python)

Containerization: Docker

Cloud Provider: AWS

Infrastructure as Code: Terraform (raw resources, no EKS module)

Container Orchestration: Kubernetes (EKS)

Packaging: Helm

CI/CD: GitHub Actions

State Management: S3 + DynamoDB (Terraform backend)

⚙️ CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline automates the entire workflow:

Checkout source code

Build Docker image

Push image to Docker Hub

Authenticate with AWS

Deploy application to AWS EKS using Helm

Secrets are securely managed using GitHub Actions Secrets, and a dedicated IAM user with least privilege access is used for deployments.

🚢 Kubernetes & Helm Deployment

Application deployed to AWS EKS

Helm charts used instead of raw YAML for:

Better version control

Easy upgrades and rollbacks

Cleaner configuration management

Application verified using Kubernetes services and port-forwarding

Swagger UI (/docs) accessible after deployment

💰 Cost Optimization Strategy

To avoid unnecessary cloud charges, the project follows a:

Deploy → Test → Destroy approach

All runtime infrastructure (EKS, EC2, VPC, Load Balancers) is destroyed after validation

Terraform backend (S3 + DynamoDB) is retained for safe state management

AWS Billing and Free Tier usage verified after teardown

📸 Screenshots

The repository includes screenshots for:

Successful GitHub Actions pipeline

Docker image pushed to Docker Hub

Kubernetes pods and services running

Helm release status

FastAPI Swagger UI

🧠 Key Learnings

Terraform remote backend and state locking

Raw EKS resource management vs Terraform modules

Kubernetes scheduling constraints on small nodes

Helm-based application lifecycle management

Secure CI/CD automation using GitHub Actions

AWS cost monitoring and cleanup best practices

▶️ How to Run (High-Level)

Build and push Docker image

Provision AWS infrastructure using Terraform

Configure kubeconfig for EKS

Deploy application using Helm

Validate application

Destroy infrastructure after testing

🔗 Repository

GitHub:
https://github.com/mandloidev246/fastapi-devops-eks

✅ Project Status

✔️ Completed
✔️ Fully automated
✔️ Cost-safe teardown verified
