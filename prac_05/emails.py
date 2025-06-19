def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        email_to_name[email] = extract_name(email)
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    name_part = email.split("@")[0].title()
    return name_part

main()