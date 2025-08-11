import openai
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_openai(messages, model="gpt-3.5-turbo", temperature=0.7, max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error with OpenAI API: {str(e)}"
