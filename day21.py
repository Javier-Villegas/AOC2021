from timeit import default_timer as timer

def roll(dice) -> (int,int):
    new_dice = dice+1 if dice < 100 else 1
    return dice, new_dice

def dirac_game(s,p,turn) -> (int,int):
    res = [0,0]
    if (s[0],s[1],p[0],p[1],turn) in cache.keys():
        return cache[(s[0],s[1],p[0],p[1],turn)]


    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                n_p = [p[0],p[1]]
                n_p[turn]+= (i+j+k)
                if n_p[turn]>10:
                    n_p[turn]-=10
                
                if s[turn]+n_p[turn]>=21:
                    res[turn]+=1
                    continue
                if turn==0:
                    r1,r2 = dirac_game([s[0]+n_p[turn],s[1]],[n_p[turn],p[1]],1)
                else:
                    r1,r2 = dirac_game([s[0],s[1]+n_p[turn]],[p[0],n_p[turn]],0)

                res[0]+= r1*1
                res[1]+= r2*1
    
    cache[(s[0],s[1],p[0],p[1],turn)] = (res[0],res[1]) 
    return (res[0],res[1])

global cache
cache = {}
if __name__=='__main__':
    start = timer()
    pos = []
    score = [0,0]
    with open('inputs/day21.txt') as f:
        for line in f:
            pos.append(int(line[:-1].rsplit(' ',1)[1]))
    pos2 = [pos[0],pos[1]]
    dice = 1
    rolls = 0
    max_score = 0
    while max_score < 1000:
        for i in range(len(pos)):
            if max_score < 1000:
                new_pos = pos[i]
                for _ in range(3):
                    r,dice = roll(dice)
                    new_pos += r

                if new_pos > 10:
                    new_pos = new_pos%10
                    if new_pos==0:
                        new_pos = 10
                pos[i] = new_pos
                rolls+=3
                score[i]+=pos[i]
                if score[i] > max_score:
                    max_score = score[i]
    print(f'Result part 1: {rolls*sorted(score)[0]}')
    score = [0,0]
    r1,r2 = dirac_game(score,pos2,0)
    if r1 > r2:
        print(f'Result part 2: {r1}')
    else:
        print(f'Result part 2: {r2}')
    print(f'Elapsed time: {timer()-start} seconds')
