import argparse
from llm_review_package.llm_review.reviewers.python_reviewer import review_python_code

from colorama import init, Fore, Style

init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="Review a Python file using LLM")
    parser.add_argument("file_path", help="Path to the Python file")
    args = parser.parse_args()

    with open(args.file_path, "r", encoding="utf-8") as f:
        code = f.read()

    print("[debug] File loaded, size:", len(code), "chars")

    reviews = review_python_code(code)
    print(f"[debug] Received {len(reviews)} reviews from LLM")

    for i, (fn, review) in enumerate(reviews, 1):
        print("=" * 80)
        print(f"🔍 Function #{i}")
        print("-" * 80)
        print(fn.strip())
        print("\n💬 Review:")
        print(Style.BRIGHT + Fore.BLUE + review.strip())
        print("=" * 80)

if __name__ == "__main__":
    main()
