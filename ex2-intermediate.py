def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    D = [
        [0, 8943, 8019, 3652, 10545],
        [8943, 0, 2619, 6317, 2078],
        [8019, 2619, 0, 5836, 4939],
        [3652, 6317, 5836, 0, 7825],
        [10545, 2078, 4939, 7825, 0]
    ]

    co2 = 0.020

    def generate_routes(route, remaining_ports):
        if not remaining_ports:
            # Base case: calculate emissions and print route
            distance = 0
            for i in range(len(route) - 1):
                distance += D[route[i]][route[i+1]]
            emissions = distance * co2
            print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)
        else:
            # Recursive case: try each remaining port next
            for i in range(len(remaining_ports)):
                new_route = route + [remaining_ports[i]]
                new_remaining = remaining_ports[:i] + remaining_ports[i+1:]
                generate_routes(new_route, new_remaining)

    # Start recursion with Panama fixed as first port (index 0)
    generate_routes([0], list(range(1, len(portnames))))

main()
