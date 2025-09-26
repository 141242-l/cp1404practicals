"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    score = float(input("Enter score: "))
    print(evaluate_score(score))

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} - {evaluate_score(random_score)}")


if __name__ == "__main__":
    main()