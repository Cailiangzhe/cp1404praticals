
MIN_SCORE = 0
MAX_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90
MENU = """
    (G)et a valid score (must be 0-100 inclusive)
    (P)rint result (copy or import your function to determine the result from score.py)
    (S)how stars (this should print as many stars as the score)
    (Q)uit
"""

def main():
    score = get_valid_score()
    print(MENU)
    choice = input("Choice:").lower()
    while choice != "q":
        if choice == "g":
            score = get_valid_score()
        elif choice == "p":
            print(determine_score_category(score))
        elif choice == "s":
            print_stars(score)
        else:
            print("Invalid")
        print(MENU)
        choice = input("Choice:").lower()
    print("Bye")

def get_valid_score():
    """Get a valid score"""
    score = int(input("Enter a valid score（0-100）："))
    while score < 0 or score > 100:
        print("Score must be 0-100 inclusive")
        score = int(input("Enter a valid score（0-100）："))
    return score

def determine_score_category(score):
    """Determine the result for the given score"""
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print stars"""
    print("*" * int(score))

main()