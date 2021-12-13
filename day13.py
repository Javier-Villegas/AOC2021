from timeit import default_timer as timer
import numpy as np

def fold(mapp,inst):
    (axis,pos) = inst.split('=')
    pos = int(pos)
    if axis[-1]=='y':
        return mapp[0:pos,:] | mapp[:pos:-1,:]
    else:
        return mapp[:,0:pos] | mapp[:,:pos:-1]
if __name__=='__main__':
    start = timer()
    with open('inputs/day13.txt','r') as f:
        manual = f.read()
    (sheet, instructions) = manual.split('\n\n')
    sheet = np.array(list(map(lambda x: list(map(int,x)) ,list(map(lambda x: x.split(','),sheet.split('\n'))))))
    (dimy,dimx) = (np.max(sheet[:,1])+1,np.max(sheet[:,0])+1)
    if dimx%2==0:
        dimx+=1
    if dimy%2==0:
        dimy+=1
    mapp = np.zeros((dimy,dimx)).astype(bool)
    mapp[sheet[:,1],sheet[:,0]] = True

    instructions = instructions.split('\n')[:-1]
    mapp = fold(mapp,instructions[0])
    print(f'Result part 1: {mapp.sum()}')
    for inst in instructions[1:]:
        mapp = fold(mapp,inst)

    print('Result part 2:')
    np.set_printoptions(linewidth=200)
    text = np.full(mapp.shape,'.')
    text[mapp] = '#'
    print(text)
    end = timer()
    print(f'Elapsed time: {end-start} seconds')

