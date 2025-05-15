# Review for `../llm-turkish-faq-bot/src/qa_pipeline.py`

## Function #1

```python
def ask_model(prompt, model="qwen:7b-chat", timeout=90):
    try:
        log(f"🟡 [DEBUG] {model} modeline prompt gönderiliyor (timeout={timeout}s)...")
        log(f"📤 [PROMPT]:\n---\n{prompt}\n---")

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": True,
            },
            stream=True,
            timeout=timeout + 30
        )
        response.raise_for_status()

        final_output = ""
        for line in response.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                final_output += data.get("response", "")
            except json.JSONDecodeError:
                continue

        log(f"📥 [RESPONSE]:\n---\n{final_output[:500]}...\n---")
        return final_output

    except requests.Timeout:
        return f"{model} zaman aşımına uğradı."
    except Exception as e:
        return f"{model} hatası: {str(e)}"


def guess_document_type(summary: str) -> str:
    json_path = os.path.join(os.path.dirname(__file__), 'document_types.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        document_types = json.load(f)

    summary_lower = summary.lower()
    for doc_type, keywords in document_types.items():
        if any(keyword in summary_lower for keyword in keywords):
            return doc_type
    return "general"

def ask_llm(question, context):
    log("Tüm işlem Qwen modeli ile başlatılıyor...")

    # Belge türünü context üzerinden tahmin et
    doc_type = guess_document_type(context)

    # Prompt oluştur
    prompt = build_prompt(question, context, doc_type, INSTRUCTIONS)

    # Cevabı al
    return ask_model(prompt, model="qwen:7b-chat", timeout=150)
```
**💬 Review:**

[Error]

---
