# 🤖 LLM Code Review Bot

A lightweight, fully local code reviewer powered by [Ollama](https://ollama.com) and Qwen/Mistral.  
It parses your Python files, extracts functions, and uses an LLM to suggest improvements — just like a real dev reviewer.

![PyPI](https://img.shields.io/pypi/v/llm-review)
![License](https://img.shields.io/pypi/l/llm-review)
![Downloads](https://img.shields.io/pypi/dm/llm-review)

---

## ✨ Features
- Extracts Python functions using regex (no AST or tree-sitter required)
- Sends each function to a local LLM (via Ollama) for review
- CLI-based — no frontend required
- Outputs reviews in your terminal with color formatting
- Supports `--save` to export results as Markdown
- Completely offline — free & private

---

## 🚀 Quickstart

### 1. Install Ollama and run a model
```bash
ollama run qwen:7b-chat
```

### 2. Install the CLI tool
```bash
pip install llm-review
```

### 3. Run the review
```bash
llm-review path/to/your_folder --save
```

Markdown files will be saved to `./reviews`.

---

## 📦 Example Output

```bash
📂 Reviewing: myfile.py
🔍 Function #1
💬 Review:
Consider improving error handling and adding a docstring.
```

---

## 🛠 Tech Stack

- 🧠 Local LLMs via [Ollama](https://ollama.com)
- 🐍 Python 3.10+
- 🎨 [Rich](https://github.com/Textualize/rich) for CLI formatting
- ✍️ Markdown output

---

## 📌 Roadmap

- [x] Batch folder review
- [x] Markdown export
- [ ] GitHub PR bot integration
- [ ] HTML output
- [ ] Model selection via `--model` flag

---

## 🤝 Contributing

Pull requests, issues, and feature ideas are welcome!

---

> Made with ❤️ by [@ErenErenturk](https://github.com/ErenErenturk)
