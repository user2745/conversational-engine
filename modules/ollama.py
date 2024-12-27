import requests


llm_url="http://localhost:11434/api/chat"
model_name="phi3"

def query_ollama(prompt):
    # Query the Ollama API
    try:
        print(f"OLLAMA Prompt: {prompt}")
        response = requests.post(
            llm_url,
            json={
                "model": model_name,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
            }
        )
        return response.json()["message"]["content"]
    except Exception as e:
        return f"Error querying nova: {e}"