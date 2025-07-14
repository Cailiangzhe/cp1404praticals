from guitar import Guitar
FILENAME = "guitars.csv"

def main():
    """A program to show guitars"""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted by year:")
    display_guitars(guitars)

    new_guitars = add_guitars()
    guitars.extend(new_guitars)
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display the list of guitars."""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def add_guitars():
    """Prompt user to enter new guitars, return them as a list."""
    new_guitars = []
    print("Enter your new guitars (leave name blank to finish):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

if __name__ == "__main__":
    main()