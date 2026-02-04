from functions.run_python_file import run_python_file

print("Result for 'main.py")
print(run_python_file("calculator", "main.py"))

print("Result for main with args:")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Result for pkg's calculator:")
print(run_python_file("calculator", "tests.py"))

print("Result for '../main.py':")
print(run_python_file("calculator", "../main.py"))

print("Result for 'does not exist':")
print(run_python_file("calculator", "nonexistent.py"))

print("Result for 'lorem':")
print(run_python_file("calculator", "lorem.txt"))