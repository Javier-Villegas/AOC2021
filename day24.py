from timeit import default_timer as timer

if __name__=='__main__':
    start = timer()
    with open('inputs/day24.txt','r') as f:
        inst = f.readlines()
    div = list(filter(lambda x: x[:5]=='div z',inst))
    div = list(map(lambda x: int(x[6:-1]),div))
    add_x = list(filter(lambda x: x[:5]=='add x' and x[6]!='z',inst)) 
    add_x = list(map(lambda x: int(x[6:-1]),add_x))
    add_y = list(filter(lambda x: x[:5]=='add y' and x[6]!='w',inst)) 
    add_y = add_y[2::3]
    add_y = list(map(lambda x: int(x[6:-1]),add_y))

    rels = []
    prev = []
    for i in range(14):
        if div[i]==1:
            prev.append(i)
        else:
            prev_num = prev.pop()
            rels.append((prev_num,i,add_y[prev_num]+add_x[i]))

    MONAD = 14*[9]
    for p1,p2,offset in rels:
        if offset >= 0:
            MONAD[p1] = 9-offset
        else:
            MONAD[p2] = 9+offset
    print('Result part 1: ' +''.join([str(x) for x in MONAD]))
    
    MONAD = 14*[1]
    for p1,p2,offset in rels:
        if offset <= 0:
            MONAD[p1] = 1-offset
        else:
            MONAD[p2] = 1+offset
    print('Result part 2: ' +''.join([str(x) for x in MONAD]))
    print(f'Elapsed time: {timer()-start} seconds') 
