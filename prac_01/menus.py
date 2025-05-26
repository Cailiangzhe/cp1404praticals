def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

name = input("Enter name: ")
display_menu()
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    display_menu()
    choice = input(">>> ").upper()
print("Finished.")