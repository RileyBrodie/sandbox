"""Riley Brodie"""
min_length = 2
max_length = 10

password = str(input("Enter a password"))
while len(password) not in range(min_length, max_length + 1):
    print("please enter a password between 2 and 10 characters")
    password = str(input("Enter a password"))

print("*" * len(password))
