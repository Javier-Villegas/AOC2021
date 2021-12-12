from timeit import default_timer as timer

def part1(tunnels:dict) -> list[list]:
    building = [['start']]
    res = []
    while building:
        for p in building.copy():
            building.remove(p)
            lobby = p[-1]
            for wayout in tunnels[lobby]:     
                if wayout == 'end':
                    res.append(p+[wayout])
                elif ((wayout.isupper()) or wayout not in p) and wayout in tunnels.keys():
                    building.append(p+[wayout])
    return res

def part2(tunnels:dict) -> list[list]:
    building = [[True,'start']]
    res = []
    while building:
        for p in building.copy():
            building.remove(p)
            lobby = p[-1]
            for wayout in tunnels[lobby]:     
                if wayout != 'start':
                    if wayout == 'end':
                        res.append(p[1:]+[wayout])
                        
                    elif (
                            (wayout.isupper()) or (p[0] or wayout not in p)
                            ) and wayout in tunnels.keys():
                        if p[0] and wayout.islower() and p.count(wayout)==1:
                            building.append([False]+p[1:]+[wayout])
                        else:
                            building.append(p+[wayout])

    return res

if __name__=='__main__':
    start = timer()
    tunnels = {}
    with open('inputs/day12.txt','r') as f:
        for line in f:
            (lobby,wayout) = line[:-1].split('-')
            if lobby not in tunnels.keys():
                tunnels[lobby] = []
            if wayout not in tunnels.keys():
                tunnels[wayout] = []
            tunnels[wayout].append(lobby)
            tunnels[lobby].append(wayout)
    res1 = len(part1(tunnels))
    print(f'Result part 1: {res1}')
    res2 = len(part2(tunnels))
    print(f'Result part 2: {res2}')
    end = timer()
    print(f'Elapsed time: {end-start} seconds')

