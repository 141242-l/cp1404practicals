"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(determine_result(score))

    import random
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} - {determine_result(random_score)}")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()