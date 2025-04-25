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

# AI Assisted Code Editor - Installation and Usage Guide
## Deployment with Kubernetes
### Steps

1. Convert your OpenAI API key to Base64 format:
   ```bash
   echo -n "your_api_key" | base64
   ```

2. In the kubernetes/deployment.yaml file, replace the api-key value in the openai-api-secret Secret resource with the Base64 encoded API key you obtained from the above command.
3.  Build the Docker image and push it to a Docker registry accessible by your Kubernetes cluster:
   docker build -t ai-code-generator .
   # If using local Minikube:
   minikube image load ai-code-generator
   # Or if using a registry like Docker Hub:
   docker tag ai-code-generator your_username/ai-code-generator
   docker push your_username/ai-code-generator
   ```

4. If using an external registry, update the image name in the kubernetes/deployment.yaml file.
5. Create the Kubernetes resources:
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml

6. Check the service status:
   kubectl get svc ai-code-generator


7. You can access the application via the LoadBalancer IP or NodePort. If using Minikube:
   minikube service ai-code-generator

## Troubleshooting

- **API Key Error**: Make sure the correct API key is defined in the `.env` file or in the Kubernetes secret.
- **Port Conflict**: If port 5000 is being used by another application, change the port number in the `app.py` file or in the Docker/Kubernetes configurations.
- **Kubernetes Pod Error**: Check the pod status with the `kubectl describe pod <pod-name>` command.

## Notes

- The application runs on port 5000 by default.
- The Kubernetes configuration uses the `/health` endpoint to check the health status of the application.
- Review security settings and take necessary precautions before using in a production environment.