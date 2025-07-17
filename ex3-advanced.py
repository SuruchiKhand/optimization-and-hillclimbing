import math
import random  # for generating random mountains

# generate random mountains
w = [.05, random.random() / 3, random.random() / 3]
h = [1. + math.sin(1 + x / .6) * w[0] + math.sin(-.3 + x / 9.) * w[1] + math.sin(-.2 + x / 30.) * w[2] for x in range(100)]

def climb(x, h):
    summit = False

    while not summit:
        summit = True  # assume we've reached the summit unless a better spot is found

        # check all positions within 5 steps left and right (excluding x itself)
        for x_new in range(max(0, x - 5), min(99, x + 6)):
            if h[x_new] > h[x]:
                x = x_new  # move to higher point
                summit = False
                break      # optional: stop at first higher point found

    return x

def main(h):
    x0 = random.randint(1, 98)  # avoid boundaries
    x = climb(x0, h)
    return x0, x

x0, x = main(h)
print(f"Venla started at {x0} and got to {x}")


# import math
# import random  # for generating random mountains

# # generate random mountains
# w = [.05, random.random() / 3, random.random() / 3]
# h = [1. + math.sin(1 + x / .6) * w[0] + math.sin(-.3 + x / 9.) * w[1] + math.sin(-.2 + x / 30.) * w[2] for x in range(100)]

# def climb(x):
#     # keep climbing until we've found a summit
#     summit = False

#     # edit here
#     while not summit:
#         summit = True
#         for x_new in range(max(0, x-5), min(99, x+5)):
#             if h[x_new] > h[x]:
#                 x = x_new         # here is higher, go here 
#                 summit = False    # and keep going
#     return x
# def main():
#     x0 = random.randint(1,98)
#     x = climb(x0)
#     return x0, x

# x0, x = main()
# print(f"Venla started at {x0} and got to {x}")

