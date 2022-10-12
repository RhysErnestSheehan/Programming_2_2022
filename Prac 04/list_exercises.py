"""Rhys Sheehan CP1404 Prac 04 List exercises"""

numbers = []
for number in range(5):
    number = input("Pick a number: ")
    numbers.append(number)

print(f"The first number is", numbers[0])
print(f"The last number is", numbers[4])
print(f"The smallest number is", min(numbers))
print(f"The largest number is", max(numbers))
