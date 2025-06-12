numbers = []
for i in range(5):
    number = int(input("Number:"))
    numbers.append(number)
print(f"The first number is {0}\n"
      f"The last number is {-1}\n"
      f"THe smallest number is {min(numbers)}\n"
      f"THe largest number is {max(numbers)}\n"
      f"The average of the numbers is {sum(numbers)/len(numbers):.1f}")
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please enter your username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")