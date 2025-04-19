# app.py

import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from models.job import Job
from ai_service import generate_code_with_openai

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Generate code based on the provided prompt"""
    prompt = request.form.get('prompt')
    
    if not prompt:
        return jsonify({
            'error': 'Prompt is required'
        }), 400
    
    try:
        # Generate code using OpenAI
        title, code = generate_code_with_openai(prompt)
        
        return jsonify({
            'title': title,
            'code': code
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/health')
def health():
    """Health check endpoint for Kubernetes"""
    return jsonify({
        'status': 'healthy'
    })

if __name__ == '__main__':
    # Get port from environment variable or use 5000 as default
    port = int(os.environ.get('PORT', 5000))
    # Run the Flask app
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('DEBUG', 'False').lower() == 'true')