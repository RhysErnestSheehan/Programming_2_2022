"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A value error will occur when a user enters an invalid number.
2. When will a ZeroDivisionError occur?
A Zero Division Error occurs when a user tries to divide a number by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could add error checking to check if the denominator is a zero and if it is ask the user to enter a number that is
greater than or less than zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
