#a
from codecs import BOM_BE

name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

#b
file = open("name.txt", "r")
name = file.read()
file.close()
print(f"Hi {name}!")

#c
with open("number.txt", "r") as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
    total = first_number + second_number
    print(total)

#d
total = 0
with open("number.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        total += number
print(total)
