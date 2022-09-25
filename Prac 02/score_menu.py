"""Rhys Sheehan CP1404 Prac 02 Score Menu"""

MENU = """R - Print result
              S - Print Stars- 
              Q - Quit"""


def main():
    score = int(input("What is your score?: "))
    if score < 0 or score > 100:
        print("Invalid score, try again")
        score = input("What is your score?: ")
    else:
        print(MENU)
    choice = input("What is your choice?: ").upper()
    while choice != "Q":
        if choice == "R":
            print(print_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thanks for playing")


def print_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    if score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


def print_stars(score):
    print(score * "*")


main()
