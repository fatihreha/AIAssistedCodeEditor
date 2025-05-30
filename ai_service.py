# ai_service.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=api_key)

def generate_code_with_gemini(prompt):
    """Generate Python code and title based on the provided prompt using Google Gemini API
    
    Args:
        prompt (str): User's prompt for code generation
        
    Returns:
        tuple: (title, code) where title is a string and code is a string
    """
    # System message to guide the AI response format
    system_message = """
    You are an AI code generator assistant. Your task is to generate Python code based on the user's prompt.
    The code should be based on the following Job class template:
    
    ```python
    class Job(Task):
        def run(self):
            asset = self.asset
            self.output['detail'] = []  # Detailed result from job
            self.output['compact'] = []  # Short result from job
            self.output['video'] = []  # Steps, commands, etc. for doing the job
            
        def calculate_score(self):
            # Score ranges:
            # - score == 1: information
            # - 1 < score < 4: low
            # - 4 <= score < 7: medium
            # - 7 <= score < 9: high
            # - 9 <= score < 11: critical
            self.score = self.param['max_score']
    ```
    
    Your response should include:
    1. A short, meaningful title for the code (prefixed with "Title: ")
    2. The complete Python code implementation that extends the Job class
    
    The code should be well-documented with English comments and follow best practices.
    """
    
    try:
        # Initialize the Gemini model
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
        }
        model = genai.GenerativeModel(model_name='gemini-1.5-pro', 
                                     generation_config=generation_config)
        
        # Create a chat session
        chat = model.start_chat(history=[])
        
        # Send the system message and user prompt
        response = chat.send_message(f"{system_message}\n\nUser prompt: {prompt}")
        
        # Extract the response content
        content = response.text
        
        # Parse the title and code from the response
        title_line = None
        code_block = ""
        
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith("Title:"):
                title_line = line.replace("Title:", "").strip()
            elif line.strip().startswith("```python"):
                # Find the end of the code block
                start_idx = i + 1
                end_idx = None
                for j in range(start_idx, len(lines)):
                    if lines[j].strip().startswith("```"):
                        end_idx = j
                        break
                
                if end_idx:
                    code_block = "\n".join(lines[start_idx:end_idx])
                    break
        
        # If no title was found, use a default title
        if not title_line:
            title_line = "Generated Python Code"
            
        # If no code block was found, use the entire response
        if not code_block:
            code_block = content
        
        return title_line, code_block
        
    except Exception as e:
        raise Exception(f"Error generating code: {str(e)}")


def list_available_models():
    """List all available Gemini models for the configured API key"""
    try:
        models = genai.list_models()
        return [model.name for model in models]
    except Exception as e:
        return f"Error listing models: {str(e)}"