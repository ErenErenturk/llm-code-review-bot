# 🤖 LLM Code Review Bot

A lightweight, fully local code reviewer powered by [Ollama](https://ollama.com) and Qwen/Mistral.  
It parses your Python files, extracts functions, and uses an LLM to suggest improvements — just like a real dev reviewer.

## ✨ Features
- Extracts Python functions using regex (no AST or tree-sitter required)
- Sends each function to a local LLM (via Ollama) for review
- CLI-based — no frontend required
- Outputs reviews in your terminal
- Completely offline — free & private

## 🚀 Quickstart

### 1. Install Ollama and run the model
```bash
ollama run qwen:7b-chat
```

### 2. Clone and install requirements
```bash
git clone https://github.com/ErenErenturk/llm-code-review-bot.git
cd llm-code-review-bot
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the review tool
```bash
python review.py path/to/your_script.py
```

You'll see something like:
```
[debug] Extracted 3 functions
[debug] LLM response: "This function could benefit from more error handling..."
```

## 🛠 Tech Stack

- 🧠 Qwen via [Ollama](https://ollama.com)
- 🐍 Python 3.10+
- 🧪 Regex-based function extraction
- 📦 No external APIs

---

## 📌 Future Plans
- Batch review folders
- GitHub PR comments
- Save review results to Markdown or HTML

---

## 🧠 Example Output

> 💬 “Consider adding a docstring and improving exception handling for this function.”

---

Contributions welcome — feedback, PRs, and ideas are all appreciated!
