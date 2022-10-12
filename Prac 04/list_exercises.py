"""Rhys Sheehan CP1404 Prac 04 List exercises"""

numbers = []
for number in range(5):
    number = input("Pick a number: ")
    numbers.append(number)

print(f"The first number is", numbers[0])
print(f"The last number is", numbers[4])
print(f"The smallest number is", min(numbers))
print(f"The largest number is", max(numbers))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("What is your username?: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")