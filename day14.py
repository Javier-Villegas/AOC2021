from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':
    start = timer()
    with open('inputs/day14.txt','r') as f:
        (polymer,pairs) = f.read().split('\n\n')
        polymer = list(polymer)
        compounds = set(pairs)
        pairs = list(map(lambda x:x.replace(' -> ',''),pairs.split('\n')))

    compounds.remove('\n')
    compounds.remove(' ')
    compounds.remove('-')
    compounds.remove('>')

    counter1 = {}
    for c in compounds:
        counter1[c] = 0
    counter2 = counter1.copy()
    
    chains = {}
    pairs.pop()

    combinations = []
    for c1 in compounds:
        for c2 in compounds:
            combinations.append(c1+c2)
            chains[c1+c2] = 0 
    for i in range(len(polymer)-1):
        chains[polymer[i]+polymer[i+1]] += 1

    chains_upd = chains.copy()

    for _ in range(10):
        for pair in pairs:
            aux = chains[pair[0:2]]
            chains_upd[pair[0:2]] -= aux
            chains_upd[pair[0]+pair[2]] += aux
            chains_upd[pair[2]+pair[1]] += aux
        for k in chains.keys():
            chains[k] = chains_upd[k]
        chains_upd = chains.copy()

    for comb in combinations:
        counter1[comb[0]] += chains[comb]

    max = min = 0
    for c in compounds:
        if min > counter1[c] or min == 0:
            min = counter1[c]
            cmin = c
        if max < counter1[c]:
            max = counter1[c]
            cmax = c
    if polymer[-1]==cmax:
        max += 1
    if polymer[-1]==cmin:
        min += 1

    print(f'Result part 1: {max-min}')

    for _ in range(30):
        for pair in pairs:
            aux = chains[pair[0:2]]
            chains_upd[pair[0:2]] -= aux
            chains_upd[pair[0]+pair[2]] += aux
            chains_upd[pair[2]+pair[1]] += aux
        for k in chains.keys():
            chains[k] = chains_upd[k]
        chains_upd = chains.copy()

    for comb in combinations:
        counter2[comb[0]] += chains[comb]

    max = min = 0
    for c in compounds:
        if min > counter2[c] or min == 0:
            min = counter2[c]
        if max < counter2[c]:
            max = counter2[c]

    if polymer[-1]==cmax:
        max += 1
    if polymer[-1]==cmin:
        min += 1
    print(f'Result part 2: {max-min}')
    end = timer()
    print(f'Elapsed time: {end-start} seconds')
