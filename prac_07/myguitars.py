from guitar import Guitar

FILENAME = "guitars.csv"

def load_guitars(filename):
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def save_guitars(filename, guitars):
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

