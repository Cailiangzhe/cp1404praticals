#1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

#2
in_file = open("name.txt", "r")
name_in_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_in_file}!")

#3
with open("numbers.txt", "r") as file:
    lines = file.readlines()
    result = int(lines[0]) + int(lines[1])
    print(result)

#4
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
    print(total)
