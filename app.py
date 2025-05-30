# app.py

import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from models.job import Job
# Import Gemini instead of OpenAI
from ai_service import generate_code_with_gemini

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

# Import Gemini instead of OpenAI
from ai_service import generate_code_with_gemini

@app.route('/generate', methods=['POST'])
def generate():
    """Generate code based on the provided prompt"""
    prompt = request.form.get('prompt')
    
    if not prompt:
        return render_template('index.html', error='Prompt is required')
    
    try:
        # Use Gemini instead of OpenAI
        title, code = generate_code_with_gemini(prompt)
        
        return render_template('index.html', title=title, code=code)
    except Exception as e:
        return render_template('index.html', error=str(e))

@app.route('/health')
def health():
    """Health check endpoint for Kubernetes"""
    return jsonify({
        'status': 'healthy'
    })

@app.route('/list-models')
def list_models():
    models = ai_service.list_available_models()
    return jsonify(models)

if __name__ == '__main__':
    # Get port from environment variable or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    # Run the Flask app
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('DEBUG', 'False').lower() == 'true')