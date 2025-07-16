portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
route = [0]
ports = list(range(1, len(portnames)))

# def permutations(route, ports):
#     if not ports:
#         print('.'.join([portnames[i] for i in route]))
#     else:
#         for i in range(len(ports)):
#             next_route = route +[ports[i]]
#             remaining_ports = ports[:i] + ports[i+1:]
#             permutations(next_route, remaining_ports)
# permutations([0], list(range(1, len(portnames))))

def permutations(route, ports):
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])
permutations([0], list(range(1,len(portnames))))