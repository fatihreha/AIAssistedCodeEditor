# AI Assisted Code Generator

This project is an AI-powered code generator assistant that works through a simple web interface. Users can enter a prompt, and the AI model generates Python code based on that prompt, using the provided Job class as a foundation.

## Features

- Web interface for entering prompts
- AI-powered code generation using OpenAI API
- Generated code based on the provided Job class template
- Meaningful title generation for each code snippet
- Kubernetes deployment support

## Technical Components

1. **Model Integration**
   - Uses OpenAI API for code generation
   - Custom system prompt to guide the AI response format

2. **Python Integration**
   - Flask web application for the user interface
   - OpenAI API integration for AI model access

3. **Output Processing**
   - Parses code blocks from the model response
   - Extracts and displays the title

4. **Deployment**
   - Docker containerization
   - Kubernetes deployment configuration

## Setup and Installation

### Prerequisites

- Python 3.8+
- Docker
- Kubernetes cluster or Minikube
- OpenAI API key

### Local Development

1. Clone the repository
2. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python app.py
   ```

### Docker Build

```
docker build -t ai-code-generator .
```

## CI/CD, Docker and Kubernetes Integration

This project provides automatic code synchronization from GitHub to GitLab, Docker image creation with GitLab CI/CD pipeline, and automatic deployment to a Kubernetes cluster.

### Automatic Code Synchronization
- Code changes are automatically mirrored from GitHub to GitLab using GitHub Actions.
- For details, see the `CI_CD_KURULUM.md` file.

### GitLab CI/CD Pipeline
- The code is built, tested, and the Docker image is automatically created and pushed to the registry.
- After the pipeline is completed, automatic deployment to the Kubernetes cluster is performed.
- Pipeline configuration: `.gitlab-ci.yml`

### Docker
- The `Dockerfile` is located in the project root directory.
- The Docker image is automatically built and used during the pipeline.

### Kubernetes
- Deployment and service definitions are located in the `kubernetes/` directory.
- The necessary config and secret settings for automatic deployment to the Kubernetes cluster are used in the pipeline.

### Setup and Detailed Information
- For all integration and automation steps, please review the `CI_CD_KURULUM.md` file.

### Kubernetes Deployment

```
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

## Usage

1. Access the web interface
2. Enter your prompt in the text area
3. Click "Generate Code"
4. View the generated code and title

## Project Structure

```
.
├── app.py                  # Main Flask application
├── templates/              # HTML templates
│   └── index.html          # Main web interface
├── static/                 # Static assets
│   └── style.css           # CSS styles
├── config.py               # Configuration settings
├── ai_service.py           # AI integration service
├── models/                 # Model definitions
│   └── job.py              # Job class implementation
├── Dockerfile              # Docker configuration
├── kubernetes/             # Kubernetes configuration
│   ├── deployment.yaml     # Deployment configuration
│   └── service.yaml        # Service configuration
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (not in git)
```

## License

MIT