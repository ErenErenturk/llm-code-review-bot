import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen:7b-chat"

def ask_llm(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        print("[debug] Sending request to Ollama...")
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        print("[debug] LLM response received:", result.get("response", "[No content]")[:200])
        return result.get("response", "[No response]")
    except Exception as e:
        print(f"[LLM Error] {e}")
        return "[Error]"
