from timeit import default_timer as timer
import numpy as np
from scipy.signal import convolve2d

def part1(m):
    sel = np.zeros(m.shape).astype(bool)
    sel[1:-1,1:-1] = (m[1:-1,1:-1] < m[2:,1:-1]) & (m[1:-1,1:-1] < m[:-2,1:-1]) & (m[1:-1,1:-1] < m[1:-1,2:]) & (m[1:-1,1:-1] < m[1:-1,:-2])
    sel[0,1:-1] = (m[0,1:-1] < m[1,1:-1]) & (m[0,1:-1] < m[0,2:]) & (m[0,1:-1] < m[0,:-2])
    sel[-1,1:-1] = (m[-1,1:-1] < m[-2,1:-1]) & (m[-1,1:-1] < m[-1,2:]) & (m[-1,1:-1] < m[-1,:-2])
    sel[1:-1,0] = (m[1:-1,0] < m[1:-1,1]) & (m[1:-1,0] < m[2:,0]) & (m[1:-1,0] < m[:-2,0])
    sel[1:-1,-1] = (m[1:-1,-1] < m[1:-1,-2]) & (m[1:-1,-1] < m[2:,-1]) & (m[1:-1,-1] < m[:-2,-1])
    sel[0,0] = (m[0,0] < m[1,0]) & (m[0,0] < m[0,1])
    sel[0,-1] = (m[0,-1] < m[1,-1])&(m[0,-1] < m[0,-2])
    sel[-1,0] = (m[-1,0] < m[-1,1])&(m[-1,0]<m[-2,0])
    sel[-1,-1] = (m[-1,-1] < m[-2,-1])&(m[-1,-1]<m[-1,-2])
    return (m[sel]+1).sum()

def add_rm_ady(basins,row,col):
    res = 1
    basins[row,col] = False
    if col > 0 and basins[row,col-1]:
        res += add_rm_ady(basins,row,col-1)
    if col < basins.shape[1]-1 and basins[row,col+1]:
        res += add_rm_ady(basins,row,col+1)
    if row > 0 and basins[row-1,col]:
        res += add_rm_ady(basins,row-1,col)
    if row < basins.shape[0]-1 and basins[row+1,col]:
        res += add_rm_ady(basins,row+1,col)
    return res

def part2(m):
    res = []
    basins = np.zeros(m.shape).astype(bool)
    basins[:,1:] |= (m[:,1:] < m[:,:-1])
    basins[:,:-1] |= (m[:,:-1] < m[:,1:])
    basins[1:,:] |= (m[1:,:] < m[:-1,:])
    basins[:-1,:] |= (m[:-1,:] < m[1:,:])
    print(basins.sum())

    for row in range(basins.shape[0]):
        for col in range(basins.shape[1]):
            if basins[row,col]:
                res.append(add_rm_ady(basins,row,col))
    print(sorted(res)) 
    return np.multiply.reduce(sorted(res,reverse=True)[0:3])
if __name__=='__main__':

    start = timer()
    res1 = 0
    with open('inputs/day9.txt') as f:
        m = f.readlines()
    m = np.array(list(map(lambda x: list(x)[:-1],m))).astype(int)
    res1 = part1(m)

    res2 = part2(m)
    print(f'Result part 1: {res1}')
    print(f'Result part 2: {res2}')
    end = timer()
    print(f'Elapsed time: {end-start} seconds')
