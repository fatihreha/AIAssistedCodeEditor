# AI Assisted Code Editor - Kurulum ve Çalıştırma Rehberi

Bu rehber, AI Assisted Code Editor projesini yerel ortamda çalıştırmanız, Docker ile konteynerize etmeniz ve Kubernetes üzerinde dağıtmanız için gereken adımları içermektedir.

## Yerel Ortamda Çalıştırma

### Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- OpenAI API anahtarı

### Adımlar

1. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

2. `.env` dosyası oluşturun ve OpenAI API anahtarınızı ekleyin:
   ```bash
   echo "OPENAI_API_KEY=sizin_api_anahtariniz" > .env
   ```

3. Uygulamayı çalıştırın:
   ```bash
   python app.py
   ```

4. Tarayıcınızda `http://localhost:5000` adresine giderek uygulamaya erişebilirsiniz.

## Docker ile Çalıştırma

### Gereksinimler

- Docker
- OpenAI API anahtarı

### Adımlar

1. Docker imajını oluşturun:
   ```bash
   docker build -t ai-code-generator .
   ```

2. Docker konteynerini çalıştırın:
   ```bash
   docker run -p 5000:5000 -e OPENAI_API_KEY=sizin_api_anahtariniz ai-code-generator
   ```

3. Tarayıcınızda `http://localhost:5000` adresine giderek uygulamaya erişebilirsiniz.

## Kubernetes ile Dağıtım

### Gereksinimler

- Kubernetes cluster (Minikube, Docker Desktop Kubernetes, veya bulut tabanlı bir Kubernetes hizmeti)
- kubectl komut satırı aracı
- OpenAI API anahtarı

### Adımlar

1. OpenAI API anahtarınızı Base64 formatına dönüştürün:
   ```bash
   echo -n "sizin_api_anahtariniz" | base64
   ```

2. `kubernetes/deployment.yaml` dosyasında, `openai-api-secret` Secret kaynağındaki `api-key` değerini, yukarıdaki komuttan elde ettiğiniz Base64 kodlu API anahtarı ile değiştirin.

3. Docker imajını oluşturun ve Kubernetes cluster'ınızın erişebileceği bir Docker registry'sine gönderin:
   ```bash
   docker build -t ai-code-generator .
   # Eğer yerel Minikube kullanıyorsanız:
   minikube image load ai-code-generator
   # Veya Docker Hub gibi bir registry kullanıyorsanız:
   docker tag ai-code-generator kullanici_adiniz/ai-code-generator
   docker push kullanici_adiniz/ai-code-generator
   ```

4. Eğer harici bir registry kullanıyorsanız, `kubernetes/deployment.yaml` dosyasındaki imaj adını güncelleyin.

5. Kubernetes kaynaklarını oluşturun:
   ```bash
   kubectl apply -f kubernetes/deployment.yaml
   ```

6. Servisin durumunu kontrol edin:
   ```bash
   kubectl get svc ai-code-generator
   ```

7. LoadBalancer IP'si veya NodePort üzerinden uygulamaya erişebilirsiniz. Minikube kullanıyorsanız:
   ```bash
   minikube service ai-code-generator
   ```

## Sorun Giderme

- **API Anahtarı Hatası**: `.env` dosyasında veya Kubernetes secret'ında doğru API anahtarının tanımlandığından emin olun.
- **Port Çakışması**: 5000 portu başka bir uygulama tarafından kullanılıyorsa, `app.py` dosyasında veya Docker/Kubernetes yapılandırmalarında port numarasını değiştirin.
- **Kubernetes Pod Hatası**: `kubectl describe pod <pod-adı>` komutu ile pod durumunu kontrol edin.

## Notlar

- Uygulama varsayılan olarak 5000 portunda çalışır.
- Kubernetes yapılandırması, uygulamanın sağlık durumunu kontrol etmek için `/health` endpoint'ini kullanır.
- Üretim ortamında kullanmadan önce güvenlik ayarlarını gözden geçirin ve gerekli önlemleri alın.