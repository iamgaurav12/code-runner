import os
import sys

def check_syntax(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    try:
        compile(code, file_path, 'exec')
        print(f"No syntax errors in {file_path}")
    except SyntaxError as e:
        print(f"Syntax error in {file_path}: {e}")

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        check_syntax(arg)
