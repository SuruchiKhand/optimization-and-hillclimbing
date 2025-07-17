import random

def main():
    prob_cat = 0.20
    if random.random() < prob_cat:
        print("cat")
    else:
        print("dog")
main()