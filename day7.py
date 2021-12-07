import numpy as np
from timeit import default_timer as timer
if __name__=='__main__': 
    start = timer()
    with open('inputs/day7.txt','r') as f:
        input = np.fromstring(f.readline(),sep=',',dtype=int)
    print(f'Part 1: {np.abs((input-int(np.median(input).round()))).sum()}')
    
    
   # res = 0
   # last = -1
   # for j in range(int(np.mean(input).round()),1,-1):
   #     for i in np.abs(input-j):
   #         res += np.add.reduce(range(i+1))
   #     if res > last and last!=-1:
   #         res = last
   #         break
   #     last = res
   #     res = 0
    res = 0
    for i in np.abs(input-int(np.mean(input))):
        res += np.add.reduce(range(i+1))
    print(f'Part 2: {res}')
    end = timer()
    print(f'Elapsed time: {end-start} seconds')
