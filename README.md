# LLM Code Review Bot

This tool analyzes Python code files, extracts functions, and uses a local LLM (e.g. Mistral via Ollama) to suggest improvements.

## Setup
```
pip install -r requirements.txt
ollama run mistral
```

## Run (CLI)
Use the modules in `reviewers/` directly.

## Run (Web)
```
streamlit run app.py
```

## Notes
- Requires `tree-sitter` Python bindings
- Must build language support:
```
git clone https://github.com/tree-sitter/tree-sitter-python
mkdir -p build
python -c "from tree_sitter import Language; Language.build_library('build/my-languages.so', ['tree-sitter-python'])"
```
