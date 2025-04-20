# CI/CD Pipeline Setup Instructions

This document explains the setup of the CI/CD pipeline for automatic code synchronization from GitHub to your new GitLab project and Kubernetes deployment. All instructions and links have been updated for your new GitLab repository and SSH keys.

## Automatic Synchronization from GitHub to GitLab

1. Create a new project in GitLab (e.g., `git@gitlab.com:GITLAB_KULLANICI_ADI/YENI_PROJE_ADI.git`)
2. Add the following repository secrets in GitHub:
   - `GITLAB_USERNAME`: Your GitLab username
   - `GITLAB_SSH_PRIVATE_KEY`: SSH private key generated for your new GitLab project

### Creating an SSH Key

```bash
# Create SSH key
ssh-keygen -t ed25519 -C "github-to-gitlab-mirror"

# View public key (to add to your new GitLab project)
cat ~/.ssh/id_ed25519.pub

# View private key (to add to GitHub secrets)
cat ~/.ssh/id_ed25519
```

3. Add the generated public key to your new GitLab account (Settings > SSH Keys)

## GitLab CI/CD Pipeline Configuration

1. Add the following CI/CD variables in your new GitLab project (Settings > CI/CD > Variables):
   - `CI_REGISTRY_USER`: Docker registry username
   - `CI_REGISTRY_PASSWORD`: Docker registry password
   - `KUBE_CONFIG`: Kubernetes config file encoded with Base64

### Encoding Kubernetes Config File to Base64

#### On Linux/macOS
```bash
cat ~/.kube/config | base64 -w 0
```

#### On Windows (PowerShell)
```powershell
[System.Convert]::ToBase64String([System.IO.File]::ReadAllBytes("$env:USERPROFILE\.kube\config"))
```

Copy the resulting base64 string and add it as the `KUBE_CONFIG` variable in your GitLab project's CI/CD Variables section.

## Kubernetes Deployment

1. Create the required namespace in your Kubernetes cluster:

```bash
kubectl create namespace ai-applications
```

2. Add your OpenAI API key as a Kubernetes secret:

```bash
kubectl create secret generic openai-api-secret --from-literal=api-key=YOUR_OPENAI_API_KEY -n ai-applications
```

## Pipeline Workflow

1. When you push code to GitHub, GitHub Actions automatically mirrors the code to your new GitLab project
2. The GitLab CI/CD pipeline is triggered and performs the following steps:
   - Build and test the code
   - Build the Docker image and push it to the registry
   - Deploy to Kubernetes

Bu yapılandırma sayesinde, sadece GitHub'a kod push etmeniz yeterlidir. Değişiklikleriniz otomatik olarak yeni GitLab projenize yansıtılacak ve oradan da Kubernetes cluster'ınıza deploy edilecektir.