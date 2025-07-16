portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# Distance matrix
D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0]
]

co2 = 0.020  # Emissions per km per ton

def calculate_emissions(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += D[route[i]][route[i+1]]
    return distance * co2

def find_best_route(route, ports):
    if not ports:
        emissions = calculate_emissions(route)
        return emissions, route
    else:
        best_emissions = float('inf')
        best_route = []
        for i in range(len(ports)):
            next_route = route + [ports[i]]
            remaining = ports[:i] + ports[i+1:]
            emissions, candidate_route = find_best_route(next_route, remaining)
            if emissions < best_emissions:
                best_emissions = emissions
                best_route = candidate_route
        return best_emissions, best_route

def main():
    initial_route = [0]  # Start at PAN
    remaining_ports = list(range(1, len(portnames)))  # [1, 2, 3, 4]
    smallest, bestroute = find_best_route(initial_route, remaining_ports)
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()

# portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# D = [
#         [0,8943,8019,3652,10545],
#         [8943,0,2619,6317,2078],
#         [8019,2619,0,5836,4939],
#         [3652,6317,5836,0,7825],
#         [10545,2078,4939,7825,0]
#     ]

# co2 = 0.020

# smallest = 1000000
# bestroute = None

# def permutations(route, ports):
#     global smallest, bestroute
#     if len(ports) < 1:
#         score = co2 * sum(D[i][j] for i, j in zip(route[:-1], route[1:]))
#         if score < smallest:
#             smallest = score
#             bestroute = route
#     else:
#         for i in range(len(ports)):
#             permutations(route+[ports[i]], ports[:i]+ports[i+1:])

# def main():
#     permutations([0], list(range(1, len(portnames))))

#     print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

# main()
