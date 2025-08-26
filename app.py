from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Store your key securely

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.json.get('topic', '')
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a detailed blog post about: {topic}",
        temperature=0.7,
        max_tokens=600,
    )
    content = response.choices[0].text.strip()

    return jsonify({'content': content})

if __name__ == '__main__':
    app.run(debug=True)
