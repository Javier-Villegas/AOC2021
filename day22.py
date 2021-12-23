from timeit import default_timer as timer
from bisect import insort
import numpy as np
def merge_pieces(pos_pieces):
    for p1 in pos_pieces:
        for p2 in pos_pieces:
            if p1==p2:
                continue
            if p1[0]==p2[0] and p1[1]==p2[1] and p1[2]==p2[2] and p1[3]==p2[3]:
                pos_pieces.remove(p1)
                pos_pieces.remove(p2)
                if p1[4]<p2[4]:
                    pos_pieces.append([p1[0],p1[1],p1[2],p1[3],p1[4],p2[5]])
                else:
                    pos_pieces.append([p1[0],p1[1],p1[2],p1[3],p2[4],p1[5]])
                break
            elif p1[0]==p2[0] and p1[1]==p2[1] and p1[4]==p2[4] and p1[5]==p2[5]:
                pos_pieces.remove(p1)
                pos_pieces.remove(p2)
                if p1[2]<p2[2]:
                    pos_pieces.append([p1[0],p1[1],p1[2],p2[3],p1[4],p1[5]])
                else:
                    pos_pieces.append([p1[0],p1[1],p2[2],p1[3],p1[4],p1[5]])
                break
            elif p1[2]==p2[2] and p1[3]==p2[3] and p1[4]==p2[4] and p1[5]==p2[5]:
                pos_pieces.remove(p1)
                pos_pieces.remove(p2)
                if p1[0]<p2[0]:
                    pos_pieces.append([p1[0],p2[1],p1[2],p1[3],p1[4],p1[5]])
                else:
                    pos_pieces.append([p2[0],p1[1],p1[2],p1[3],p1[4],p1[5]])
                break
    return pos_pieces

def get_overlap(r1,r2) -> list:
    if (    
        (r1[0] <= r2[0] <= r1[1]) 
        or (r2[0] <= r1[0] <=r2[1])) and(
        (r1[2] <= r2[2] <= r1[3]) 
        or (r2[2] <= r1[2] <=r2[3])) and(
        (r1[4] <= r2[4] <= r1[5]) 
        or (r2[4] <= r1[4] <=r2[5])):
        x = [0,0]
        x[0]=r1[0] if r2[0]-r1[0]<0 else r2[0]
        x[1]=r1[1] if r1[1]-r2[1]<0 else r2[1]
        y = [0,0]
        y[0]=r1[2] if r2[2]-r1[2]<0 else r2[2]
        y[1]=r1[3] if r1[3]-r2[3]<0 else r2[3]
        z = [0,0]
        z[0]=r1[4] if r2[4]-r1[4]<0 else r2[4]
        z[1]=r1[5] if r1[5]-r2[5]<0 else r2[5]
        return (x[0],x[1],y[0],y[1],z[0],z[1])
    return []

def intersect_cube(cube,olap) -> list:
    pieces = []
    if cube[0] < olap[0]:
        pieces.append([cube[0],olap[0]-1,cube[2],cube[3],cube[4],cube[5]])
    if cube[1] > olap[1]:
        pieces.append([olap[1]+1,cube[1],cube[2],cube[3],cube[4],cube[5]])
    if cube[2] < olap[2]:
        pieces.append([olap[0],olap[1],cube[2],olap[2]-1,cube[4],cube[5]])
    if cube[3] > olap[3]:
        pieces.append([olap[0],olap[1],olap[3]+1,cube[3],cube[4],cube[5]])
    if cube[4] < olap[4]:
        pieces.append([olap[0],olap[1],olap[2],olap[3],cube[4],olap[4]-1])
    if cube[5] > olap[5]:
        pieces.append([olap[0],olap[1],olap[2],olap[3],olap[5]+1,cube[5]])        
    return pieces

if __name__=='__main__':
    start = timer()
    reactor = []
    cubes = np.zeros((101,101,101)).astype(bool)
    with open('inputs/day222.txt','r') as f:
        for line in f.readlines():
            state,rest = line[:-1].split(' ',1)
            state = True if state=='on' else False
            x,y,z = rest.split(',')
            x = list(map(int,x[2:].split('..')))
            y = list(map(int,y[2:].split('..')))
            z = list(map(int,z[2:].split('..')))
            reactor.append([x[0],x[1],y[0],y[1],z[0],z[1],state])
            x[0] = x[0]+50 if x[0]>-50 else 0
            x[1] = x[1]+50 if x[1]<50 else 100
            y[0] = y[0]+50 if y[0]>-50 else 0
            y[1] = y[1]+50 if y[1]<50 else 100
            z[0] = z[0]+50 if z[0]>-50 else 0
            z[1] = z[1]+50 if z[1]<50 else 100
            cubes[x[0]:x[1]+1,y[0]:y[1]+1,z[0]:z[1]+1] = state
    on = 0
    #for i in range(len(reactor)-1,-1,-1):
    #for i in range(len(reactor)-1,-1,-1):
    #    if reactor[i][-1]:
    #        print(i)
    #        print(reactor[i])
    #        vol=(reactor[i][1]-reactor[i][0])*(reactor[i][3]-reactor[i][2])*(reactor[i][5]-reactor[i][4])
    #        for j in range(i+1,len(reactor)):
    #            if (
    #                    (reactor[i][0] <= reactor[j][0] <= reactor[i][1]) 
    #                    or (reactor[j][0] <= reactor[i][0] <=reactor[j][1])) and(
    #                    (reactor[i][2] <= reactor[j][2] <= reactor[i][3]) 
    #                    or (reactor[j][2] <= reactor[i][2] <=reactor[j][3])) and(
    #                    (reactor[i][4] <= reactor[j][4] <= reactor[i][5]) 
    #                    or (reactor[j][4] <= reactor[i][4] <=reactor[j][5])):
    #                x = [0,0]
    #                x[0]=reactor[i][0] if reactor[j][0]-reactor[i][0]<0 else reactor[j][0]
    #                x[1]=reactor[i][1] if reactor[i][1]-reactor[j][1]<0 else reactor[j][1]
    #                y = [0,0]
    #                y[0]=reactor[i][2] if reactor[j][2]-reactor[i][2]<0 else reactor[j][2]
    #                y[1]=reactor[i][3] if reactor[i][3]-reactor[j][3]<0 else reactor[j][3]
    #                z = [0,0]
    #                z[0]=reactor[i][4] if reactor[j][4]-reactor[i][4]<0 else reactor[j][4]
    #                z[1]=reactor[i][5] if reactor[i][5]-reactor[j][5]<0 else reactor[j][5]
    #                vol -= (x[1]-x[0])*(y[1]-y[0])*(z[1]-z[0])
    #                print()
    #                print(reactor[i])
    #                print(reactor[j])
    #                print(x)
    #                print(y)
    #                print(z)
    #                print()
    #                if vol <=0:
    #                    vol = 0
    #        on+=vol                
    print(on)
    pos_pieces = [[reactor[0][0],reactor[0][1],reactor[0][2],
                  reactor[0][3],reactor[0][4],reactor[0][5]]]
    for cube in reactor[1:]:
        print(cube)
        if cube[-1]:
            new_pieces = []
            for p in pos_pieces:
                overlap = get_overlap(cube[:-1],p)
                if overlap:
                    new_pieces.extend(intersect_cube(cube[:-1],overlap))
            if not new_pieces:
                pos_pieces.append(cube[:-1])
                continue
            #new_pieces = merge_pieces(new_pieces)
            any_overlap = True
            while any_overlap:
                any_overlap = False
                for n in new_pieces.copy():
                    piece_overlap = False
                    for p in pos_pieces.copy():
                        overlap = get_overlap(n,p)
                        if overlap:
                            any_overlap = True
                            piece_overlap = True
                            new_pieces.remove(n)
                            new_pieces.extend(intersect_cube(n,overlap))
                            break
                    if not piece_overlap:
                        pos_pieces.append(n)
                        new_pieces.remove(n)
            #    new_pieces = merge_pieces(new_pieces)
            pos_pieces.extend(new_pieces)

        else:
            for p in pos_pieces.copy():
                overlap = get_overlap(cube[:-1],p)
                if overlap:
                    new_pieces = intersect_cube(p,overlap)
                    pos_pieces.remove(p)
                    for np in new_pieces:
                        pos_pieces.append(np)
        #pos_pieces = merge_pieces(pos_pieces)

    print(intersect_cube([0,10,0,10,0,10],[3,6,3,6,3,6]))
    print(cubes.sum()) 

    for p in pos_pieces:
        on+=(p[1]-p[0])*(p[3]-p[2])*(p[5]-p[4])     
    print(on)
