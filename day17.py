from timeit import default_timer as timer

if __name__=='__main__':
    start = timer()
    with open('inputs/day17.txt','r') as f:
        target = f.read()[13:-1].split(', ')
        target = [list(map(int,x[2:].split('..'))) for x in target]
    
    # Part 1
    y = 0
    vymax = -(target[1][0]+1)
    vy = vymax
    ymax = 0
    while y > target[1][0]:
        y+=vy
        vy-=1
        if y > ymax:
            ymax = y
    print(f'Result part 1: {ymax}')

    vxmax = target[0][1]
    vymin = target[1][0]
    # Part 2\
    initial_vel = 0
    for vx0 in range(1,vxmax+1):
        for vy0 in range(vymin,vymax+1):
            vx = vx0
            vy = vy0
            y = x = 0

            while y >= target[1][0] and x <= target[0][1]:
                y+=vy
                x+=vx
                if y >= target[1][0] and y <= target[1][1] and x >= target[0][0] and x <= target[0][1]:
                    initial_vel+=1
                    break
                if vx:
                    vx-=1
                vy-=1
    print(f'Result part 2: {initial_vel}')
    print(f'Elapsed time: {timer()-start} seconds')
