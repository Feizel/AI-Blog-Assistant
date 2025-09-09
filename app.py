from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env

app = Flask(__name__)
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest-topics', methods=['POST'])
def suggest_topics():
    try:
        interests = request.json.get('interests', '')
        if not interests:
            return jsonify({'error': 'Interests are required'}), 400

        payload = {
            "model": "sonar",
            "messages": [
                {"role": "user", "content": f"Based on these interests: {interests}, suggest 5 unique and engaging blog topic ideas that combine these interests in creative ways. Format as a numbered list with brief explanations."}
            ],
            "temperature": 0.8,
            "max_tokens": 400
        }
        
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(PERPLEXITY_URL, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"API Error: {response.status_code} - {response.text}")
        response.raise_for_status()
        
        content = response.json()['choices'][0]['message']['content'].strip()
        return jsonify({'content': content})

    except Exception as e:
        print(f"Error suggesting topics: {e}")
        return jsonify({'error': 'Failed to suggest topics'}), 500

@app.route('/proofread', methods=['POST'])
def proofread():
    try:
        text = request.json.get('text', '')
        if not text:
            return jsonify({'error': 'Text is required'}), 400

        payload = {
            "model": "sonar",
            "messages": [
                {"role": "user", "content": f"Proofread this text for grammar, spelling, clarity, and flow. Provide specific suggestions for improvement:\n\n{text}"}
            ],
            "temperature": 0.3,
            "max_tokens": 500
        }
        
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(PERPLEXITY_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        content = response.json()['choices'][0]['message']['content'].strip()
        return jsonify({'content': content})

    except Exception as e:
        print(f"Error proofreading: {e}")
        return jsonify({'error': 'Failed to proofread'}), 500

@app.route('/polish-draft', methods=['POST'])
def polish_draft():
    try:
        text = request.json.get('text', '')
        if not text:
            return jsonify({'error': 'Text is required'}), 400

        payload = {
            "model": "sonar",
            "messages": [
                {"role": "user", "content": f"As a writing assistant, help polish this human-written blog draft. Suggest improvements for flow, structure, word choice, and engagement while preserving the author's voice and style:\n\n{text}"}
            ],
            "temperature": 0.4,
            "max_tokens": 500
        }
        
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(PERPLEXITY_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        content = response.json()['choices'][0]['message']['content'].strip()
        return jsonify({'content': content})

    except Exception as e:
        print(f"Error polishing draft: {e}")
        return jsonify({'error': 'Failed to polish draft'}), 500

@app.route('/analyze-tone', methods=['POST'])
def analyze_tone():
    try:
        text = request.json.get('text', '')
        if not text:
            return jsonify({'error': 'Text is required'}), 400

        payload = {
            "model": "sonar",
            "messages": [
                {"role": "user", "content": f"Analyze the tone and style of this human-written text. Describe the current tone, target audience, and suggest adjustments if needed for better audience connection:\n\n{text}"}
            ],
            "temperature": 0.3,
            "max_tokens": 400
        }
        
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(PERPLEXITY_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        content = response.json()['choices'][0]['message']['content'].strip()
        return jsonify({'content': content})

    except Exception as e:
        print(f"Error analyzing tone: {e}")
        return jsonify({'error': 'Failed to analyze tone'}), 500

@app.route('/suggest-headlines', methods=['POST'])
def suggest_headlines():
    try:
        text = request.json.get('text', '')
        if not text:
            return jsonify({'error': 'Text is required'}), 400

        payload = {
            "model": "sonar",
            "messages": [
                {"role": "user", "content": f"Based on this human-written blog content, suggest 5 compelling headlines that would attract readers while accurately representing the content:\n\n{text}"}
            ],
            "temperature": 0.7,
            "max_tokens": 300
        }
        
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(PERPLEXITY_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        content = response.json()['choices'][0]['message']['content'].strip()
        return jsonify({'content': content})

    except Exception as e:
        print(f"Error suggesting headlines: {e}")
        return jsonify({'error': 'Failed to suggest headlines'}), 500

@app.route('/check-readability', methods=['POST'])
def check_readability():
    try:
        text = request.json.get('text', '')
        if not text:
            return jsonify({'error': 'Text is required'}), 400

        payload = {
            "model": "sonar",
            "messages": [
                {"role": "user", "content": f"Analyze this human-written text for readability. Check sentence length, paragraph structure, use of jargon, and overall accessibility. Provide specific suggestions to improve readability:\n\n{text}"}
            ],
            "temperature": 0.3,
            "max_tokens": 400
        }
        
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(PERPLEXITY_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        content = response.json()['choices'][0]['message']['content'].strip()
        return jsonify({'content': content})

    except Exception as e:
        print(f"Error checking readability: {e}")
        return jsonify({'error': 'Failed to check readability'}), 500

if __name__ == '__main__':
    app.run(debug=True)