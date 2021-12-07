import numpy as np
from timeit import default_timer as timer

if __name__=="__main__":
    start = timer()
    with open('inputs/day1.txt','r') as f:
        inp = np.array(f.readlines()).astype(int)
    # Part 1
    print(f'Result part1: {(inp[:-1] < inp[1:]).sum()}')
    
    # Part 2 
    sum = inp[:-2]+inp[1:-1]+inp[2:]
    print(f'Result part2: {(sum[:-1] < sum[1:]).sum()}')
    end = timer()

    print(f'Total time: {end-start} seconds')
