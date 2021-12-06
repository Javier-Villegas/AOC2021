import numpy as np
from timeit import default_timer as timer

if __name__=='__main__':
    start = timer()
    states = [0,0,0,0,0,0,0,0,0]
    with open('inputs/day6.txt') as f:
        input = list(map(int,f.readline().split(sep=',')))
        for i in range(9):
            states[i] = input.count(i)
    for i in range(80):
        aux = states[0]
        states[:-1] = states[1:]
        states[8] = aux
        states[6] += aux
    print(np.sum(states))
    for i in range(256-80):
        aux = states[0]
        states[:-1] = states[1:]
        states[8] = aux
        states[6] += aux
    print(np.sum(states))
    end = timer()
    print(f'Elapsed time: {end-start} seconds')
