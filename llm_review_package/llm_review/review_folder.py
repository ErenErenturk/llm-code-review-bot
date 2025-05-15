import os
import argparse
from llm_review_package.llm_review.reviewers.python_reviewer import review_python_code
from rich.console import Console
from rich.progress import track
from rich.text import Text

console = Console()

def find_python_files(folder):
    py_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".py") and not file.startswith(".venv"):
                py_files.append(os.path.join(root, file))
    return py_files

def save_review(filename, reviews):
    os.makedirs("reviews", exist_ok=True)
    out_path = os.path.join("reviews", os.path.basename(filename).replace(".py", ".md"))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Review for `{filename}`\n\n")
        for i, (fn, review) in enumerate(reviews, 1):
            f.write(f"## Function #{i}\n\n")
            f.write("```python\n" + fn.strip() + "\n```\n")
            f.write(f"**💬 Review:**\n\n{review.strip()}\n\n---\n")
    console.print(f"[green]💾 Saved review to {out_path}[/]")

def main():
    parser = argparse.ArgumentParser(description="Review all Python files in a folder using LLM")
    parser.add_argument("folder_path", help="Path to the folder")
    parser.add_argument("--save", action="store_true", help="Save each review to markdown")
    args = parser.parse_args()

    files = find_python_files(args.folder_path)
    console.print(f"[bold cyan]📦 Found {len(files)} Python files[/]")

    for i, filepath in enumerate(track(files, description="Reviewing files..."), 1):
        console.print(f"\n📂 [bold]Reviewing {i}/{len(files)}:[/] {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        reviews = review_python_code(code)
        console.print(f"[green]✅ Reviewed {len(reviews)} functions[/]")

        for j, (fn, review) in enumerate(reviews, 1):
            console.print("=" * 80)
            console.print(f"🔍 [bold magenta]{os.path.basename(filepath)} → Function #{j}[/]")
            console.print("-" * 80)
            console.print(fn.strip(), highlight=True)
            console.print("\n💬 [bold blue]Review:[/]")
            console.print(Text(review.strip(), style="bold blue"))
            console.print("=" * 80)

        if args.save and reviews:
            save_review(filepath, reviews)

if __name__ == "__main__":
    main()
