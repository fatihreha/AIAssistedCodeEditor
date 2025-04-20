# GitHub'dan GitLab'a Mirror İşlemi Kontrol Listesi

GitHub'dan GitLab'a değişikliklerin yansımaması durumunda aşağıdaki adımları kontrol edin:

## GitHub Tarafı Kontrolleri

1. **GitHub Secrets Ayarları**
   - GitHub repository'nizde (Settings > Secrets and variables > Actions) aşağıdaki secret'ların doğru şekilde tanımlandığından emin olun:
     - `GITLAB_USERNAME`: GitLab kullanıcı adınız
     - `GITLAB_SSH_PRIVATE_KEY`: GitLab için oluşturduğunuz SSH private key (tüm içeriği, başlangıç ve bitiş satırları dahil)

2. **GitHub Actions Workflow Durumu**
   - GitHub repository'nizde Actions sekmesine giderek `Mirror to GitLab` workflow'unun çalışma durumunu kontrol edin
   - Hata mesajlarını inceleyin ve gerekirse düzeltin

## SSH Key Kontrolleri

1. **SSH Key Doğruluğu**
   - SSH private key'in GitHub Secrets'a tam ve doğru şekilde eklendiğinden emin olun
   - SSH public key'in GitLab hesabınıza (Settings > SSH Keys) eklendiğinden emin olun

2. **SSH Key Yenileme**
   - Sorun devam ediyorsa, yeni bir SSH key çifti oluşturun:
   ```bash
   ssh-keygen -t ed25519 -C "github-to-gitlab-mirror"
   ```
   - Public key'i GitLab'a ekleyin
   - Private key'i GitHub Secrets'a ekleyin

## GitLab Tarafı Kontrolleri

1. **GitLab Repository Ayarları**
   - GitLab repository'nizin doğru şekilde oluşturulduğundan emin olun
   - Repository URL'sinin GitHub workflow dosyasında doğru belirtildiğini kontrol edin
   - GitLab repository'nizin Settings > Repository > Protected Branches ayarlarını kontrol edin ve gerekirse düzenleyin

2. **GitLab CI/CD Değişkenleri**
   - GitLab'da (Settings > CI/CD > Variables) aşağıdaki değişkenlerin doğru şekilde tanımlandığından emin olun:
     - `CI_REGISTRY_USER`: Docker registry kullanıcı adı
     - `CI_REGISTRY_PASSWORD`: Docker registry şifresi
     - `KUBE_CONFIG`: Base64 ile kodlanmış Kubernetes config dosyası

## Manuel Mirror Testi

GitHub Actions'ın düzgün çalışıp çalışmadığını test etmek için manuel olarak mirror işlemi yapabilirsiniz:

```bash
# Repository'yi klonlayın
git clone --mirror https://github.com/KULLANICI_ADI/AIAssistedCodeEditor.git
cd AIAssistedCodeEditor.git

# GitLab remote'unu ekleyin
git remote add gitlab git@gitlab.com:GITLAB_KULLANICI_ADI/AIAssistedCodeEditor.git

# GitLab'a push yapın
git push gitlab --mirror
```

Bu işlem başarılı olursa, sorun GitHub Actions yapılandırmasında olabilir. Başarısız olursa, GitLab erişim izinlerinde veya SSH key yapılandırmasında sorun olabilir.

## Diğer Kontroller

1. **Network Erişimi**
   - GitHub Actions runner'ların GitLab'a erişiminde bir network sorunu olmadığından emin olun

2. **Repository İsimleri**
   - GitHub ve GitLab'daki repository isimlerinin workflow dosyasında belirtilen isimlerle eşleştiğinden emin olun

Yukarıdaki adımları kontrol ettikten sonra sorun devam ediyorsa, GitHub Actions log'larını daha detaylı inceleyerek spesifik hata mesajlarını tespit edin ve ona göre çözüm üretin.