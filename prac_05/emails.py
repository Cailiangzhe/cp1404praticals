"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""
def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm == "n":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    """Extract name part from email"""
    name_part = email.split("@")[0].title()
    return name_part

main()