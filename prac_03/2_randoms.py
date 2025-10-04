import random

#a
print(random.randint(5, 20)) # line 1
print("Smallest: 5, largest: 20")

#b
print(random.randrange(3, 10, 2))  # line 2
print("Smallest: 3, largest: 10")
print("Could produce 4? No, because step=2, so only odd numbers 3,5,7,9")

#c
print(random.uniform(2.5, 5.5))  # line 3
print("Smallest: 2.5, largest: 5.5")

#d
random_number = random.randint(1, 100)
print(random_number)