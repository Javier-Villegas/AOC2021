from timeit import default_timer as timer
import re
from math import ceil,floor

def read_snailfish(snailfish:str) -> list:
    snailfish = snailfish[1:-1]
    first = 0
    pair = []
    brackets = 0
    if snailfish[0] != '[':
        
        aux = snailfish.split(',')
        pair.append(int(aux[0]))
        if len(aux) == 2:
            pair.append(int(aux[1]))
        else:
            pair.append(read_snailfish(snailfish[len(aux[0])+1:]))
    else: 
        for i in range(0,len(snailfish)):
            if snailfish[i] == '[':
                brackets+=1
                continue

            if snailfish[i] == ']':
                brackets-=1
                if brackets==0:
                    pair.append(read_snailfish(snailfish[first:i+1]))
                    if snailfish[i+2] != '[':
                        pair.append(int(snailfish[i+2:]))
                    else:
                        pair.append(read_snailfish(snailfish[i+2:]))
                    break
    return pair

def explode(snailfish:str,i:int) -> str:
    exploding_pair,rest = snailfish[i+1:].split(']',1)
    prev = snailfish[i-1::-1]
    exploding_pair = list(map(int,exploding_pair.split(',')))
    next_num = re.search('[0-9]{1,9}',rest)
    if next_num:
        next_num = int(next_num.group(0))
        next_num += exploding_pair[1]
        next_num = str(next_num)
        rest = re.split('[0-9]{1,9}',rest,1)
        rest = rest[0]+next_num+rest[1]

    prev_num = re.search('[0-9]{1,9}',prev)
    if prev_num:
        prev_num = int(prev_num.group(0)[::-1])
        prev_num += exploding_pair[0]
        prev_num = str(prev_num)
        prev = re.split('[0-9]{1,9}',prev,1)
        prev = prev[0]+prev_num[::-1]+prev[1]
    snailfish = prev[::-1]+'0'+rest

    return snailfish

def is_explodable(snailfish:str) -> (bool,int):
    depth = 0
    for i in range(len(snailfish)):
        if snailfish[i]=='[':
            depth+=1
            if depth==5:
                return (True,i)
        elif snailfish[i]==']':
            depth-=1
    return (False,0)

def reduce_snailfish(snailfish:str) -> str:
    explodable,index = is_explodable(snailfish)
    double_digit = re.search('[0-9]{2,9}',snailfish)
    while explodable or double_digit:
        if explodable:
            snailfish = explode(snailfish,index)
        elif double_digit:
            double_digit = double_digit.group(0)
            first = str(int(floor(int(double_digit)/2)))
            second = str(int(ceil(int(double_digit)/2)))
            one,two = re.split('[0-9]{2,9}',snailfish,1)
            snailfish = one+'['+first+','+second+']'+two
        explodable,index = is_explodable(snailfish) 
        double_digit = re.search('[0-9]{2,9}',snailfish)
    return snailfish


def add_snailfish(p1:str,p2:str) -> str:
    return '['+p1+','+p2+']'

def magnitude_snailfish(snailfish:list) -> int:
    if type(snailfish[0])==list:
        snailfish[0] = magnitude_snailfish(snailfish[0])
    if type(snailfish[1])==list:
        snailfish[1] = magnitude_snailfish(snailfish[1])
    return snailfish[0]*3+snailfish[1]*2

if __name__=='__main__':
    start = timer()
    with open('inputs/day18.txt','r') as f:
        shoal = f.readlines()
    snailfish = reduce_snailfish(shoal[0][:-1])
    for sf in shoal[1:]:
        next_snailfish = reduce_snailfish(sf[:-1])
        snailfish = reduce_snailfish(add_snailfish(snailfish,next_snailfish))
    print(f'Result part 1: {magnitude_snailfish(read_snailfish(snailfish))}')

    max_sum = 0
    for s1 in shoal:
        s1 = reduce_snailfish(s1[:-1])
        for s2 in shoal:
            s2 = reduce_snailfish(s2[:-1])
            if s1 != s2:
                temp_sum = magnitude_snailfish(read_snailfish(
                        reduce_snailfish(add_snailfish(s1,s2))
                        ))
                if temp_sum > max_sum:
                    max_sum = temp_sum
    print(f'Result part 2: {max_sum}')
    print(f'Elapsed time: {timer()-start} seconds')
