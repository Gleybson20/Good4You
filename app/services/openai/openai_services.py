# app/services/openai_services.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_resposta(mensagem: str, contexto: list) -> str:
    try:
        mensagens = [
            {"role": "system", "content": "Você é uma nutricionista virtual que cria dietas personalizadas."},
            *contexto,
            {"role": "user", "content": mensagem}
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=mensagens,
            temperature=0.7,
            max_tokens=500,
            n=1,
        )
        
        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar resposta OpenAI: {str(e)}")
