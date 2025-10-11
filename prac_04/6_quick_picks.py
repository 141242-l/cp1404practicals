import random

min_number = 1
max_number = 45
num_pre_pick = 6

num_picks = int(input("How many quick picks? "))

for _ in range(num_picks):
    numbers = []
    while len(numbers) < num_pre_pick:
        num = random.randint(min_number, max_number)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    print(" ".join(f"{num:2}" for num in numbers))