# AI Assisted Code Editor - Installation and Usage Guide

This guide provides the steps required to run the AI Assisted Code Editor project locally, containerize it with Docker, and deploy it on Kubernetes.

## Running Locally

### Requirements

- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key

### Steps

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file and add your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the application in your browser at `http://localhost:5000`.

## Running with Docker

### Requirements

- Docker
- OpenAI API key

### Steps

1. Build the Docker image:
   ```bash
   docker build -t ai-code-generator .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 -e OPENAI_API_KEY=your_api_key_here ai-code-generator
   ```

3. Access the application in your browser at `http://localhost:5000`.

## Deployment with Kubernetes

### Requirements

- Kubernetes cluster (Minikube, Docker Desktop Kubernetes, or a cloud-based Kubernetes service)
- kubectl command-line tool
- OpenAI API key

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