import argparse
import sys
import math
import logging
import os
import select

# Set up logging
log_dir = os.path.join(os.path.expanduser("~"), ".local", "state", "calcu")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "calcu.log"),
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate(expression):
    # Restrict the evaluation environment
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names['abs'] = abs
    allowed_names['round'] = round
    try:
        # evaluate the expression
        return eval(expression, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        logging.error(f"Error evaluating '{expression}': {e}")
        return f"Error: {e}"

def main():
    parser = argparse.ArgumentParser(description="calcu - A minimal calculator")
    parser.add_argument("expression", nargs=argparse.REMAINDER, help="Mathematical expression to evaluate")
    parser.add_argument("-i", "--interactive", action="store_true", help="Start interactive terminal mode")
    args = parser.parse_args()

    if args.expression:
        expr = " ".join(args.expression)
        result = calculate(expr)
        print(result)
    elif args.interactive:
        print("calcu - interactive mode (type 'exit' to quit)")
        while True:
            try:
                expr = input("calcu> ")
                if expr.strip().lower() in ('exit', 'quit'):
                    break
                if expr.strip():
                    print(calculate(expr))
            except (EOFError, KeyboardInterrupt):
                print()
                break
    else:
        # Read from stdin if piped data actually exists
        if select.select([sys.stdin,],[],[],0.0)[0]:
            expr = sys.stdin.read().strip()
            if expr:
                print(calculate(expr))
        else:
            # Launch GUI
            try:
                from calcu.ui import run_ui
                run_ui()
            except ImportError as e:
                logging.error(f"GUI failed to load: {e}")
                print(f"Error: Could not load GUI ({e}). Ensure tkinter is installed.")
                print("Use -i for interactive CLI.")

if __name__ == "__main__":
    main()
