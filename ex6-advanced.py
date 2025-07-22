import numpy as np
import random
import math

N = 100           # Landscape size (NxN)
steps = 3000      # Number of iterations per track
tracks = 50       # Number of parallel optimization tracks

# Generate a 2D function with multiple local optima
def generator(x, y, x0=0.0, y0=0.0):
    return (
        np.sin((x / N - x0) * np.pi) +
        np.sin((y / N - y0) * np.pi) +
        0.07 * np.cos(12 * (x / N - x0) * np.pi) +
        0.07 * np.cos(12 * (y / N - y0) * np.pi)
    )

def main():
    # Random offsets to shift the landscape
    x0 = np.random.random() - 0.5
    y0 = np.random.random() - 0.5

    # Create the 2D landscape
    h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)

    # Find coordinates of global maximum
    peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

    # Initialize search points randomly
    x = np.random.randint(0, N, tracks)
    y = np.random.randint(0, N, tracks)

    for step in range(steps):
        # Cooling schedule (annealing temperature)
        T = max(0, ((steps - step) / steps) ** 3 - 0.005)

        for i in range(tracks):
            # Propose new solution near current
            x_new = np.random.randint(max(0, x[i] - 2), min(N, x[i] + 3))
            y_new = np.random.randint(max(0, y[i] - 2), min(N, y[i] + 3))
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # Accept move if it's better
            if S_new > S_old:
                x[i], y[i] = x_new, y_new
            # Else accept it probabilistically (simulated annealing)
            elif T > 0:
                prob = math.exp(-(S_old - S_new) / T)
                if random.random() < prob:
                    x[i], y[i] = x_new, y_new

    # Count how many tracks found the global optimum
    hits = sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])
    print(f"{hits} tracks found the global optimum")

main()

# import numpy as np
# import random
# import math

# # Constants
# N = 100           # Landscape size (NxN)
# steps = 3000      # Number of iterations per track
# tracks = 50       # Number of parallel optimization tracks

# # Generate a 2D function with multiple local optima
# def generator(x, y, x0=0.0, y0=0.0):
#     return (
#         np.sin((x / N - x0) * np.pi) +
#         np.sin((y / N - y0) * np.pi) +
#         0.07 * np.cos(12 * (x / N - x0) * np.pi) +
#         0.07 * np.cos(12 * (y / N - y0) * np.pi)
#     )

# # Optimization function
# def run_annealing():
#     # Random offsets to shift the landscape
#     x0 = np.random.random() - 0.5
#     y0 = np.random.random() - 0.5

#     # Create the 2D landscape
#     h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)

#     # Find coordinates of global maximum
#     peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

#     # Initialize search points randomly
#     x = np.random.randint(0, N, tracks)
#     y = np.random.randint(0, N, tracks)

#     for step in range(steps):
#         # Cooling schedule (annealing temperature)
#         T = max(0, ((steps - step) / steps) ** 3 - 0.005)

#         for i in range(tracks):
#             # Propose new solution near current
#             x_new = np.random.randint(max(0, x[i] - 2), min(N, x[i] + 3))
#             y_new = np.random.randint(max(0, y[i] - 2), min(N, y[i] + 3))
#             S_old = h[x[i], y[i]]
#             S_new = h[x_new, y_new]

#             # Accept move if it's better
#             if S_new > S_old:
#                 x[i], y[i] = x_new, y_new
#             # Else accept it probabilistically (simulated annealing)
#             elif T > 0:
#                 prob = math.exp(-(S_old - S_new) / T)
#                 if random.random() < prob:
#                     x[i], y[i] = x_new, y_new

#     # Count how many tracks found the global optimum
#     hits = sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])
#     return hits

# # Test runner
# def test_runs(runs=100, required_hits=30):
#     successes = 0
#     for i in range(runs):
#         hits = run_annealing()
#         print(f"Run {i+1}: {hits} tracks found the peak")
#         if hits >= required_hits:
#             successes += 1

#     print(f"\n✅ Passed {successes}/{runs} runs with at least {required_hits} tracks finding the global optimum.")
#     if successes < runs:
#         print("⚠️  Try tuning temperature schedule or steps if needed.")

# # Run the test
# test_runs()
