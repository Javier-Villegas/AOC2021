import numpy as np
from timeit import default_timer as timer
limit = 9 

def flash(octopus,row,col,visited):
    res = 0
    if (row,col) not in visited:
        visited.append((row,col))
        res += 1
        if row > 0:
            octopus[row-1,col] += 1
            if octopus[row-1,col] > 9 and (row-1,col) not in visited:
                res += flash(octopus,row-1,col,visited)
            if col > 0:
                octopus[row-1,col-1] += 1
                if octopus[row-1,col-1] > 9 and (row-1,col-1) not in visited:
                    res += flash(octopus,row-1,col-1,visited)
            if col < limit:
                octopus[row-1,col+1] += 1
                if octopus[row-1,col+1] > 9 and (row-1,col+1) not in visited:
                    res += flash(octopus,row-1,col+1,visited)
         
        if row < limit:
            octopus[row+1,col] += 1
            if octopus[row+1,col] > 9 and (row+1,col) not in visited:
                res += flash(octopus,row+1,col,visited)
            if col > 0:
                octopus[row+1,col-1] += 1
                if octopus[row+1,col-1] > 9 and(row+1,col-1) not in visited:
                    res += flash(octopus,row+1,col-1,visited)
            if col < limit:
                octopus[row+1,col+1] += 1
                if octopus[row+1,col+1] > 9 and (row+1,col+1) not in visited:
                    res += flash(octopus,row+1,col+1,visited)
        if col > 0:
            octopus[row,col-1] += 1
            if octopus[row,col-1] > 9 and (row,col-1) not in visited:
                res += flash(octopus,row,col-1,visited)
        if col < limit:
            octopus[row,col+1] += 1
            if octopus[row,col+1] > 9 and (row,col+1) not in visited:
                res += flash(octopus,row,col+1,visited)
    return res

if __name__=='__main__':
    start = timer()
    octopus = np.zeros((limit+1,limit+1),int)
    res1 = 0
    with open('inputs/day11.txt','r') as f:
        for i,octopussy in enumerate(f):
            octopus[i,:] = list(octopussy[:-1])
    for i in range(100):
        octopus += 1
        visited = []
        for row in range(10):
            for col in range(10):
                if octopus[row,col] > 9:
                    res1 += flash(octopus,row,col,visited) 
        octopus[octopus > 9] = 0

    res2 = 100
    while(not (octopus==0).all()):
        octopus += 1
        res2 += 1
        visited = []
        for row in range(10):
            for col in range(10):
                if octopus[row,col] > 9:
                    res1 += flash(octopus,row,col,visited) 
        octopus[octopus > 9] = 0

    print(f'Result part 1: {res1}')
    print(f'Result part 2: {res2}')
    end = timer()
    print(f'Elapsed time: {end-start} seconds')
