"""Rhys Sheehan CP1404 Prac 02 Password Stars"""


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password_minimum_length = 8
    password = input("What is your new password?: ")
    while len(password) < password_minimum_length:
        print("Invalid password, please try again.")
        password = input("What is your new password?: ")
    return password


def print_asterisks(password):
    print(len(password) * "**")


main()
