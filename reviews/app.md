# Review for `../llm-turkish-faq-bot/src/app.py`

## Function #1

```python
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i+chunk_size])
    return chunks

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def query_index(index, embedding, top_k=3):
    distances, indices = index.search(embedding, top_k)
    return indices

uploaded_file = st.file_uploader("Bir PDF dosyası yükleyin", type=["pdf"])
```
**💬 Review:**

[Error]

---
