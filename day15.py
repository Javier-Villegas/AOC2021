from timeit import default_timer as timer
import numpy as np

if __name__=='__main__':
    start = timer()
    with open('inputs/day15.txt','r') as f:
        cave = np.array(list(map(lambda x: list(x[:-1]),f.readlines()))).astype(int)
    risk = 0
    (rowlim,collim) = cave.shape
    rowlim-=1
    collim-=1

    current_row = np.cumsum(cave[0,1:])
    current_col = np.cumsum(cave[1:,0])

    acc_risk = cave[1:,1:].copy()
    row = col = 1
    for row in range(len(current_col)):
        next_row = []
        for col in range(len(current_row)):
            if col:
                next_row.append(min(current_row[col]+acc_risk[row,col],next_row[col-1]+acc_risk[row,col]))
            else:
                next_row.append(min(current_row[col]+acc_risk[row,col],current_col[row]+acc_risk[row,col]))
            col+=1
        acc_risk[row,:] = next_row
        current_row = next_row
        row += 1
        col = 1
    print(f'Result part 1: {acc_risk[-1,-1]}')

    row_caves = []
    for row in range(5):
        col_caves = []
        for col in range(5):
            col_caves.append(cave+col+row)
            col_caves[col][col_caves[col] > 9] -= 9

        row_caves.append(np.concatenate(col_caves,axis=1))
    cave = np.concatenate(row_caves,axis=0)

    visited = np.zeros(cave.shape).astype(bool)
    visited[0,0] = True
    paths = {}
    paths[0,0] = 0
    while paths:
        del_path = []
        minval = 0
        path = 0
        for (key,val) in paths.items():
            cost = []
            next = []
            if key[0] < 499 and not visited[key[0]+1,key[1]]:
                cost.append(val+cave[key[0]+1,key[1]])
                next.append((key[0]+1,key[1]))
            if key[1] < 499 and not visited[key[0],key[1]+1]:
                cost.append(val+cave[key[0],key[1]+1])
                next.append((key[0],key[1]+1))
            if key[0] > 0 and not visited[key[0]-1,key[1]]:
                cost.append(val+cave[key[0]-1,key[1]])
                next.append((key[0]-1,key[1]))
            if key[1] > 0 and not visited[key[0],key[1]-1]:
                cost.append(val+cave[key[0],key[1]-1])
                next.append((key[0],key[1]-1))

            if not cost:
                del_path.append(key)
                continue

            mincost = 0 
            for i in range(len(cost)):
                if cost[i] < mincost or mincost == 0:
                    mincost = cost[i]
                    nextmin = next[i]

            if mincost < minval or minval == 0:
                minval = mincost
                path = nextmin

        for key in del_path:
            del paths[key]
        if path == (499,499):
            print(f'Result part 2: {minval}')
            break
        if path:
            paths[path] = minval
            visited[path[0],path[1]] = True

    end = timer()
    print(f'Elapsed time: {end-start}')
