"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

MIN_SCORE = 0
MAX_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90

def main():
    score = float(input("Enter score: "))
    print(determine_score_category(score))
    random_score = random.randint(MIN_SCORE,MAX_SCORE)
    print(f"Random score is:{random_score}")
    print(determine_score_category(random_score))

def determine_score_category(score):
    """Determine the result for the given score"""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"

main()
