MIN_PASSWORD = 8

def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get user's password"""
    password = input("Enter your password: ")
    while len(password) < MIN_PASSWORD:
        print(f"Password too short, at least {MIN_PASSWORD} words.")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    print("*" * len(password))

main()