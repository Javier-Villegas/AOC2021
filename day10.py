from timeit import default_timer as timer
import numpy as np
if __name__=='__main__':
    start = timer()
    openers  = ['(','[','{','<']
    openclose = {'(':')','[':']','{':'}','<':'>'}
    cost = {')':3,']':57,'}':1197,'>':25137}
    autocost = {'(':1,'[':2,'{':3,'<':4}
    res1 = res2 = 0
    autocomplete_totals = []
    with open('inputs/day10.txt','r') as f:
        for line in f:
            buffer = []
            fec = []
            autocomplete = True 
            for c in list(line[:-1]):
                if not buffer or c in openers:
                    buffer.append(c)
                elif openclose[buffer[-1]]==c:
                    del buffer[-1]
                else:
                    if not autocomplete:
                        res1 += cost[c]
                    autocomplete = False 
                    
            if autocomplete and buffer:
                total = 0
                for buf in buffer[::-1]:
                    total *= 5
                    total += autocost[buf] 
                autocomplete_totals.append(total)

    res2 = int(np.median(autocomplete_totals))
    print(f'Result part 1: {res1}')
    print(f'Result part 2: {res2}')
    end = timer()
    print(f'Elapsed time: {end-start} seconds')


