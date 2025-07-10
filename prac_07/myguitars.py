from guitar import Guitar


"""def main():
    FILENAME = "guitars.csv"
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted by year:")
    display_guitars(guitars)

    new_guitars = add_guitars()
    guitars.extend(new_guitars)

    save_guitars(FILENAME, guitars)"""


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


"""if __name__ == "__main__":
    main()"""