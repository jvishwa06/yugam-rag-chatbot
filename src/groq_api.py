import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_response(query, context):
    """Generates a response from Groq API based on event details."""
    if not GROQ_API_KEY:
        raise ValueError("Missing Groq API key! Set it in .env")

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are an AI assistant providing event-related information."},
            {"role": "user", "content": f"Query: {query}\nContext: {context}"}
        ]
    }

    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    response = requests.post(GROQ_API_URL, json=payload, headers=headers)

    # Debugging - Print full response
    print("Full API Response:", response.status_code, response.text)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except KeyError:
        print("Error: Unexpected API response format!")
        return "Sorry, I couldn't generate a response. Check API logs."
