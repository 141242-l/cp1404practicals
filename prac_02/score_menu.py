def get_valid_score():
    score = -1
    while not (0 <= score <= 100):
        score = float(input("Enter score: "))
    return score


def evaluate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score))


def main():
    score = get_valid_score()
    menu = "(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"

    print(menu)
    while (choice := input(">>> ").upper()) != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(evaluate_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(menu)
    print("Farewell!")


if __name__ == "__main__":
    main()