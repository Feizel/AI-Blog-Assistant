# AI Blog Assistant

A simple Flask app that uses the OpenAI API to generate blog content.

---

## Setup

1. Clone the repo and go into the folder:

```
git clone https://github.com/yourusername/ai-blog-assistant.git
cd ai-blog-assistant
```

2. Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or on Windows
venv\Scripts\activate
```

3. Install dependencies:

```
pip install flask openai python-dotenv
```

4. Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

5. Run the app:

```
python app.py
```

6. Open `http://127.0.0.1:5000` in your browser to use the assistant.

---

## How to Use

- Enter a blog topic.
- Click "Generate Blog Post".
- See your AI-generated content.

---

## Notes

- Don’t share your `.env` file publicly.
- Add `venv/` and `.env` to `.gitignore`.

---

Enjoy building with AI! 🚀