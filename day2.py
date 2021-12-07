from timeit import default_timer as timer
import numpy as np

if __name__=="__main__":
    start = timer()
    horiz,depth= (0,0)
    input = []
    with open('inputs/day2.txt') as f:
        while (line := f.readline()):
            line = line.split(' ')
            input.append((line[0],int(line[1]))) 
    for (inst,val) in input:
        if inst == 'forward':
            horiz += val
        elif inst == 'down':
            depth += val 
        else:
            depth -= val
    print(f'Result part 1: {horiz*depth}')

    horiz,depth,aim = (0,0,0)
    for (inst,val) in input:
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
