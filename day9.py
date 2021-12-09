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
    return ((m[sel]+1).sum(),sel)

def add_rm_ady(m,checked,row,col):
    res = 1
    checked[row,col] = True
    if col > 0 and m[row,col-1]!=9 and not checked[row,col-1]:
        res += add_rm_ady(m,checked,row,col-1)
    if col < m.shape[1]-1 and m[row,col+1]!=9 and not checked[row,col+1]:
        res += add_rm_ady(m,checked,row,col+1)
    if row > 0 and m[row-1,col]!=9 and not checked[row-1,col]:
        res += add_rm_ady(m,checked,row-1,col)
    if row < m.shape[0]-1 and m[row+1,col]!=9 and not checked[row+1,col]:
        res += add_rm_ady(m,checked,row+1,col)
    return res

def part2(m,pits):
    res = []

    checked = np.zeros(m.shape).astype(bool)
    for row in range(m.shape[0]):
        for col in range(m.shape[1]):
            if pits[row,col] and not checked[row,col]:
                res.append(add_rm_ady(m,checked,row,col))
    print(sorted(res)) 
    return np.multiply.reduce(sorted(res,reverse=True)[0:3])
if __name__=='__main__':

    start = timer()
    res1 = 0
    with open('inputs/day9.txt') as f:
        m = f.readlines()
    m = np.array(list(map(lambda x: list(x)[:-1],m))).astype(int)
    (res1,pits) = part1(m)

    res2 = part2(m,pits)
    print(f'Result part 1: {res1}')
    print(f'Result part 2: {res2}')
    end = timer()
    print(f'Elapsed time: {end-start} seconds')
