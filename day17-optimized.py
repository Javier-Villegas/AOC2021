from timeit import default_timer as timer

if __name__=='__main__':
    start = timer()
    with open('inputs/day17.txt','r') as f:
        target = f.read()[13:-1].split(', ')
        target = [list(map(int,x[2:].split('..'))) for x in target]
    
    # Part 1
    vymax = -(target[1][0]+1)
    print(f'Result part 1: {( (vymax+1) * vymax ) // 2}')
    y = 0
    vxmax = target[0][1]
    vymin = target[1][0]
    vxmin = aux = 0
    while aux < target[0][0]:
        vxmin+=1
        aux+=vxmin
    x_sol = {}
    for v in range(vxmin,vxmax+1):
        vx = v
        x = 0
        steps = 0
        val_steps = set()
        while vx != 0 and x < target[0][1]:
            x+=vx
            steps+=1
            if vx:
                vx-=1
            if x >= target[0][0] and x <= target[0][1]:
                val_steps.add(steps)
        if val_steps:
            if vx == 0:
                val_steps.add(-1)
            x_sol[v] = val_steps

    y_sol = {}
    for v in range(vymin,vymax+1):
        vy = v
        y = 0
        steps = 0
        val_steps = set()
        while y > target[1][0]:
            y+=vy
            steps+=1
            vy-=1
            if y >= target[1][0] and y <= target[1][1]:
                val_steps.add(steps)
        if val_steps:
            y_sol[v] = val_steps

    res2 = 0
    for x_step in x_sol.values():
        for y_step in y_sol.values():
            if x_step.intersection(y_step):
                res2+=1
            elif -1 in x_step and max(y_step) >= max(x_step):
                res2+=1


    # Part 2\
    print(f'Result part 2: {res2}')
    print(f'Elapsed time: {timer()-start} seconds')
