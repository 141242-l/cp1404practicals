min_length = 8
password = input("Enter password: ")
while len(password) < min_length:
    print("Password too short")
    password = input("Enter password: ")
print("*" * len(password))