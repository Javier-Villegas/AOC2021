from timeit import default_timer as timer
import numpy as np
import pandas as pd
if __name__=='__main__':
    start = timer()
    with open('inputs/day4.txt','r') as f:
        data = f.read().split(sep='\n\n')

    numbers = np.fromstring(data[0],sep=',').astype(int)
   
    # Part 1
    cards = pd.concat(
            [pd.DataFrame(data=data[1:],columns=['cards'])['cards'].apply(lambda x: np.fromstring(x.replace('\n',' '),sep=' ').astype(int).reshape((5,5))),
             pd.Series([np.zeros((5,5)).astype(bool) for x in range(len(data)-1)],name='marked')]
            ,axis=1)
    index = []
    for num in numbers:
        last_index = index
        cards['marked'] += cards['cards'].apply(lambda x: num == x)
        index = cards['marked'].apply(lambda x: any(x.sum(axis=1)==5) or any(x.sum(axis=0)==5))
        
        if not index.empty and index.sum() ==1:
            idx = cards.index[index]
            res1 = cards['cards'][idx[0]][np.invert(cards['marked'][idx[0]])].sum()*num        
    # Part 2
        elif not index.empty and index.sum() == cards.shape[0]:
            idx = cards.index[np.invert(last_index)]
            res2 = num*cards['cards'][idx[0]][np.invert(cards['marked'][idx[0]])].sum()
            break
    print(res1)
    print(res2)
    end = timer()
    
    print(f'Elapsed time: {end-start} seconds')
