import numpy as np
from timeit import default_timer as timer

if __name__=='__main__':
    start = timer()
    data = np.array([],int)
    with open('inputs/day5.txt','r') as f:
        data = np.array(f.readline().replace(' -> ',',').split(sep=',')).astype(int)
        while (line := f.readline()):
            line = np.array(line.replace(' -> ', ',').split(sep=',')).astype(int)
            data = np.append(data,line)
    data = data.reshape((int(data.shape[0]/4),4))    

    ocean = np.zeros((data[:,[0,2]].max()+1,data[:,[1,3]].max()+1))
    ocean_diag = np.copy(ocean)
    for (x1,y1,x2,y2) in data:
        if x1 == x2 and y1 == y2:
            ocean[x1,y1] += 1
        elif x1 == x2:
            if y1 < y2:
                ocean[x1,y1:y2+1] += 1
            else:
                ocean[x1,y2:y1+1] += 1
        elif y1 == y2:
            if x1 < x2:
                ocean[x1:x2+1,y1] += 1
            else:
                ocean[x2:x1+1,y1] += 1
        else:
            if y1 < y2: 
                y = np.arange(y1,y2+1)
            else:
                y = np.arange(y1,y2-1,-1)
            if x1 < x2:
                x = np.arange(x1,x2+1)
            else:
                x = np.arange(x1,x2-1,-1)
            ocean_diag[x,y] += 1

    print((ocean > 1).sum())
    print(((ocean+ocean_diag) > 1).sum())
    end = timer()
    print(f'Elapsed time: {end-start} seconds')
