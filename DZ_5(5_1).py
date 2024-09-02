import string
import keyword
name = input("Enter the variable name: ")
if not name:
    print(False)
    exit()
if name[0].isdigit():
    print(False)
    exit()
for char in name:
    if char.isupper():
        print(False)
        exit()
for char in name:
    if char in string.punctuation and char != '_':
        print(False)
        exit()
if ' ' in name:
    print(False)
    exit()
if name.count('_') > 1:
    print(False)
    exit()
if name in keyword.kwlist:
    print(False)
    exit()
print(True)
