"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_month = int(input("How many months? "))

    for month in range(1, number_of_month + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(incomes)

def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(len(incomes)):
        income = incomes[month]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month + 1, income, total))


main()