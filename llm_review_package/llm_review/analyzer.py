import re

def extract_functions(code):
    pattern = re.compile(
        r'(?:(?:@[\w\.]+\s*)*)'          # decorators (optional)
        r'(def\s+\w+\s*\(.*?\):\s*\n'    # function def line
        r'(?:\s+.+\n)+)',                # indented body
        re.MULTILINE
    )

    matches = pattern.findall(code)
    return matches

