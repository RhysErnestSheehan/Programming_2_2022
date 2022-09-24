"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit_to_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit_to_celsius(celsius)))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius_to_fahrenheit(celsius, fahrenheit)
            print("Result: {:.2f} F".format(celsius_to_fahrenheit(celsius, fahrenheit)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius, fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def fahrenheit_to_celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()