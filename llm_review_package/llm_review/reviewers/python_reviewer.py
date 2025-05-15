from llm_review_package.llm_review.analyzer import extract_functions
from llm_review_package.llm_review.llm_interface import ask_llm

def review_python_code(code):
    functions = extract_functions(code)
    print(f"[debug] Extracted {len(functions)} functions")

    reviews = []
    for fn in functions:
        print("[debug] Sending to LLM:\n", fn[:100], "...")
        prompt = f"Please review this Python function and suggest improvements:\n\n{fn}"
        review = ask_llm(prompt)
        reviews.append((fn, review))
    return reviews
