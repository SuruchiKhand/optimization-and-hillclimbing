import random

def main():
    animals = ['dogs', 'cats', 'bats']
    weights = [80, 10, 10]
    favourite = random.choices(animals, weights, k=1)[0]
    print("I love " + favourite)
main()