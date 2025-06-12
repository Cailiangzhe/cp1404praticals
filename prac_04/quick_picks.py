import random
NUMBERS_PER_PICK = 6
MAX_NUMBER = 45
MIN_NUMBER =1


def main():
    number_of_picks = int(input("How many quick picks?"))
    for i in range(number_of_picks):
        quick_pick_numbers = quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick_numbers))

def quick_pick():
    """Pick 6 random numbers"""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        picked_number = random.randint(MIN_NUMBER,MAX_NUMBER)
        if picked_number not in numbers:
            numbers.append(picked_number)
    numbers.sort()
    return numbers



main()