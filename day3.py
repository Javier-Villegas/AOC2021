import numpy as np
import pandas as pd
from timeit import default_timer as timer
if __name__=='__main__':
    start = timer()
    input = pd.read_csv('inputs/day3.txt', header=None, dtype=str)#,converters={0: lambda x: x.split()}, header=None)
    input = input[0].apply(lambda x: np.array(list(x)))
    input = np.concatenate(input.values,axis=0)
    input = input.reshape((int(input.shape[0]/12),12)).astype(int)
    sum = input.sum(axis=0)
    gamma = sum > input.shape[0]/2
    epsilon = np.invert(gamma)

    print(np.sum(np.fromiter((2**ind for ind,val in enumerate(np.flip(gamma)) if val),dtype=int))*
    np.sum(np.fromiter((2**ind for ind,val in enumerate(np.flip(epsilon)) if val),dtype=int)))

    # Part 2
    oxygen = input[input[:,0]==int(gamma[0])]
    i = 1
    while oxygen.shape[0] != 1:
        selected_bit = int(np.sum(oxygen[:,i]) >= oxygen.shape[0]/2)
        oxygen = oxygen[oxygen[:,i]==selected_bit]
        i+=1

    scrubber = input[input[:,0]==int(epsilon[0])]
    i = 1
    while scrubber.shape[0] != 1:
        selected_bit = int(np.sum(scrubber[:,i]) < scrubber.shape[0]/2)
        scrubber = scrubber[scrubber[:,i]==selected_bit]
        i+=1
    print(np.sum(np.fromiter((2**ind for ind,val in enumerate(np.flip(oxygen[0])) if val),dtype=int))*
    np.sum(np.fromiter((2**ind for ind,val in enumerate(np.flip(scrubber[0])) if val),dtype=int)))
    end = timer()
    print(f'Elapsed time: {end-start} seconds')
