import random
import math

def accept_prob(S_old, S_new, T):
    if S_new > S_old:
        return 1.0
    else:
        return math.exp(-(S_old - S_new) / T)
def accept(S_old, S_new, T):
    if random.random() < accept_prob (S_old, S_new, T):
        print(True)
    else:
        print(False)

