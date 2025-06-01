"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_number("Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = get_number("Fahrenheit:")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_number(prompt):
    """Get user"s number"""
    number=float(input(prompt))
    return number

def celsius_to_fahrenheit(celsius):
    """Calculate celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Calculate fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)

main()




