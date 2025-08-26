from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # load environment variables from .env

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # initialize OpenAI client

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        topic = request.json.get('topic', '')
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Write a detailed blog post about: {topic}"}
            ],
            temperature=0.7,
            max_tokens=600,
        )
        content = response.choices[0].message.content.strip()
        return jsonify({'content': content})

    except Exception as e:
        print(f"Error generating content: {e}")  # Log error for debugging
        return jsonify({'error': 'Failed to generate content'}), 500

if __name__ == '__main__':
    app.run(debug=True)
