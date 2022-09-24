"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(result_of_score(score))


def result_of_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    if score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


main()
