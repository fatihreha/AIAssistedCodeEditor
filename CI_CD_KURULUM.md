# CI/CD Pipeline Kurulum Talimatları

Bu belge, GitHub'dan GitLab'a otomatik kod senkronizasyonu ve Kubernetes deployment için CI/CD pipeline kurulumunu açıklar.

## GitHub'dan GitLab'a Otomatik Senkronizasyon

1. GitLab'da yeni bir proje oluşturun
2. GitHub'da aşağıdaki repository secrets'ları ekleyin:
   - `GITLAB_USERNAME`: GitLab kullanıcı adınız
   - `GITLAB_SSH_PRIVATE_KEY`: GitLab için oluşturduğunuz SSH private key

### SSH Key Oluşturma

```bash
# SSH key oluşturma
ssh-keygen -t ed25519 -C "github-to-gitlab-mirror"

# Public key'i görüntüleme (GitLab'a eklenecek)
cat ~/.ssh/id_ed25519.pub

# Private key'i görüntüleme (GitHub secrets'a eklenecek)
cat ~/.ssh/id_ed25519
```

3. Oluşturulan public key'i GitLab hesabınıza ekleyin (Settings > SSH Keys)

## GitLab CI/CD Pipeline Yapılandırması

1. GitLab'da aşağıdaki CI/CD değişkenlerini ekleyin (Settings > CI/CD > Variables):
   - `CI_REGISTRY_USER`: Docker registry kullanıcı adı
   - `CI_REGISTRY_PASSWORD`: Docker registry şifresi
   - `KUBE_CONFIG`: Base64 ile kodlanmış Kubernetes config dosyası

### Kubernetes Config Dosyasını Base64'e Dönüştürme

```bash
cat ~/.kube/config | base64 -w 0
```

## Kubernetes Deployment

1. Kubernetes cluster'ınızda gerekli namespace'i oluşturun:

```bash
kubectl create namespace ai-applications
```

2. OpenAI API anahtarınızı Kubernetes secret olarak ekleyin:

```bash
kubectl create secret generic openai-api-secret --from-literal=api-key=YOUR_OPENAI_API_KEY -n ai-applications
```

## Pipeline Çalışma Akışı

1. GitHub'a kod push ettiğinizde, GitHub Actions otomatik olarak kodu GitLab'a mirror'lar
2. GitLab CI/CD pipeline'ı tetiklenir ve aşağıdaki adımları gerçekleştirir:
   - Kod derleme ve test
   - Docker imajı oluşturma ve registry'ye push etme
   - Kubernetes'e deployment

Bu yapılandırma sayesinde, sadece GitHub'a kod push etmeniz yeterlidir. Değişiklikleriniz otomatik olarak GitLab'a yansıtılacak ve oradan da Kubernetes cluster'ınıza deploy edilecektir.