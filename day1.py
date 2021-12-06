import numpy as np
from timeit import default_timer as timer

if __name__=="__main__":
    start = timer()
    inp = np.loadtxt('inputs/day1.txt','i4')
    
    # Part 1
    print(f'Result part1: {(inp[:-1] < inp[1:]).sum()}')
    
    # Part 2 
    sum = inp[:-2]+inp[1:-1]+inp[2:]
    print(f'Result part2: {(sum[:-1] < sum[1:]).sum()}')
    end = timer()

    print(f'Total time: {end-start} seconds')
