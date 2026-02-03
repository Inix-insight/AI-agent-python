from functions.get_file_content import get_file_content

print("Result for 'lorem.txt':")
lorem = get_file_content("calculator", "lorem.txt")
print(len(lorem))
print(lorem[10001:])

print("Result for main:")
print(get_file_content("calculator", "main.py"))

print("Result for pkg's calculator:")
print(get_file_content("calculator", "pkg/calculator.py"))

print("Result for '/bin' directory:")
print(get_file_content("calculator", "/bin/cat"))

print("Result for 'does not exist':")
print(get_file_content("calculator", "pkg/does_not_exist.py"))