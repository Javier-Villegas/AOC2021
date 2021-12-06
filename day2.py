from timeit import default_timer as timer
import pandas as pd

if __name__=="__main__":
    start = timer()
    horiz,depth= (0,0)
    input = pd.read_csv('inputs/day2.txt',delimiter=' ',names=[',inst','val'])
    for (inst,val) in input.values:
        if inst == 'forward':
            horiz += val
        elif inst == 'down':
            depth += val 
        else:
            depth -= val
    print(f'Result part 1: {horiz*depth}')

    horiz,depth,aim = (0,0,0)
    for (inst,val) in input.values:
        if inst == 'forward':
            horiz += val
            depth += val*aim
        elif inst == 'down':
            aim += val
        else:
            aim -= val

    print(f'Result part 2: {horiz*depth}')
    end = timer()
    print(f'Elapsed time: {end-start}')
