import sys
import os

# --- DICTIONARY ---

SYNTAX_MAP = {
     "output_maadi": "print",
    # "what_ra_loop": "while",
}

def transpile(source_code):
    """
    Replaces custom keywords with Python keywords.
    """
    transpiled_code = source_code
    
    for custom_word, python_word in SYNTAX_MAP.items():
        transpiled_code = transpiled_code.replace(custom_word, python_word)
        
    return transpiled_code

def main():
    # 1. Check if user provided a file
    if len(sys.argv) < 2:
        print("Aiyyo! You forgot to give the file name.")
        print("Usage:blr <filename.blr>")
        return

    filename = sys.argv[1]

    # 2. check if file exists
    if not os.path.exists(filename):
        print(f"File '{filename}' illa! (not found)")
        return

    # 3. Read the custom file
    with open(filename, 'r') as file:
        source_code = file.read()

    # 4. Convert to Python
    python_code = transpile(source_code)

    # 5. Run it
    try:
        exec(python_code, {'__name__': '__main__'})
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()