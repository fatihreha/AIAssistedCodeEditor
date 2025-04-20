# GitLab CI/CD Değişkenleri Ayarlama Rehberi

Bu rehber, GitLab CI/CD pipeline'ınız için gerekli değişkenleri nasıl ayarlayacağınızı açıklar.

## Docker Registry Bilgileri

GitLab CI/CD pipeline'ınızda Docker imajlarını oluşturmak ve registry'ye push etmek için aşağıdaki değişkenleri ayarlamanız gerekiyor:

1. GitLab'da projenize gidin
2. **Settings > CI/CD > Variables** bölümüne gidin
3. Aşağıdaki değişkenleri ekleyin:

   - `CI_REGISTRY_USER`: `fatihreha`
   - `CI_REGISTRY_PASSWORD`: `551123reha.fatih`

## Kubernetes Config Dosyası

Kubernetes cluster'ınıza deployment yapabilmek için `KUBE_CONFIG` değişkenini ayarlamanız gerekiyor. Bu değişken, kubeconfig dosyanızın base64 ile kodlanmış halidir.

### KUBE_CONFIG Değişkenini Oluşturma

1. Kubernetes config dosyanızı bulun. Bu dosya genellikle şu konumda bulunur:
   - Windows: `%USERPROFILE%\.kube\config`
   - Linux/macOS: `~/.kube/config`

2. Config dosyasını base64 formatına dönüştürün:

   **Windows PowerShell'de:**
   ```powershell
   [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes((Get-Content -Path "$env:USERPROFILE\.kube\config" -Raw)))
   ```

   **Linux/macOS Terminal'de:**
   ```bash
   cat ~/.kube/config | base64 -w 0
   ```

3. Oluşturulan base64 kodlu metni kopyalayın

4. GitLab'da projenize gidin

5. **Settings > CI/CD > Variables** bölümüne gidin

6. Yeni bir değişken ekleyin:
   - Key: `KUBE_CONFIG`
   - Value: *Yukarıdaki adımda oluşturduğunuz base64 kodlu metin*
   - Type: Variable
   - Environment scope: All (default)
   - Protect variable: Evet (önerilir)
   - Mask variable: Evet (önerilir)

## Kubernetes Cluster Bağlantısını Test Etme

KUBE_CONFIG değişkenini doğru şekilde ayarladığınızı kontrol etmek için, GitLab CI/CD pipeline'ınızda aşağıdaki test job'ını çalıştırabilirsiniz:

```yaml
test-kubernetes-connection:
  stage: test
  image: bitnami/kubectl:latest
  script:
    - echo "$KUBE_CONFIG" | base64 -d > kubeconfig.yaml
    - export KUBECONFIG=./kubeconfig.yaml
    - kubectl config use-context my-cluster  # Cluster adınıza göre değiştirin
    - kubectl get nodes
  only:
    - main
```

Bu job başarıyla çalışırsa, Kubernetes cluster'ınıza bağlantı kurabildiğiniz anlamına gelir.

## Önemli Notlar

- Eğer Kubernetes cluster'ınıza erişim için farklı bir yöntem kullanıyorsanız (örneğin, servis hesabı token'ı), KUBE_CONFIG değişkeni yerine o yönteme uygun değişkenleri ayarlamanız gerekebilir.
- Kubernetes config dosyanız hassas bilgiler içerir, bu nedenle GitLab'da "Mask variable" ve "Protect variable" seçeneklerini işaretlemeniz önerilir.
- Kubernetes cluster'ınızın yapılandırmasına bağlı olarak, `.gitlab-ci.yml` dosyasındaki `kubectl config use-context my-cluster` komutunu kendi cluster context'inize göre değiştirmeniz gerekebilir.