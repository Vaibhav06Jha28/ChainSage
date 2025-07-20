import sys
from mistral_vulnerability_checker import analyze_solidity_code

def main():
    if len(sys.argv) != 2:
        print("Usage: python cli_infer.py <path_to_solidity_file>")
        sys.exit(1)

    solidity_path = sys.argv[1]

    try:
        with open(solidity_path, 'r') as f:
            code = f.read()
            result = analyze_solidity_code(code)
            print("\n--- Mistral Vulnerability Report ---\n")
            print(result)
    except FileNotFoundError:
        print(f"File not found: {solidity_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
