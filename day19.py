from timeit import default_timer as timer
from itertools import product
#import numpy as np
def transform_rotation(r1,r2) -> list:
    r = [1,2,3]
    r_new = [0,0,0]
    for i in range(3):
        if r1[i] < 0:
            ri = -r2[abs(r1[i])-1]
            if ri < 0:
                r_new[i] = -r[abs(ri)-1]
            else:
                r_new[i] = r[ri-1]
        else:
            ri = r2[r1[i]-1]
            if ri < 0:
                r_new[i] = -r[abs(ri)-1]
            else:
                r_new[i] = r[ri-1]
    return r

def search_base(scanner1,scanner2) -> (list,list):
    found = False
    pos = []
    for i,r in enumerate(rotations):
        if found:
            break
        possible_bases = dict()

        for s1 in scanner1:
        
        
            for s2 in scanner2:
                if r[0]<0:
                    c1 = s1[0]+s2[r[0]*-1-1]
                else:
                    c1 = s1[0]-s2[r[0]-1]
                    
                if r[1]<0:
                    c2 = s1[1]+s2[r[1]*-1-1]
                else:
                    c2 = s1[1]-s2[r[1]-1]
                if r[2]<0:
                    c3 = s1[2]+s2[r[2]*-1-1]
                else:
                    c3 = s1[2]-s2[r[2]-1]
                if (c1,c2,c3) in possible_bases.keys():
                    possible_bases[(c1,c2,c3)][1] += 1
                    possible_bases[(c1,c2,c3)][0].append(s1)
                    
                    if possible_bases[(c1,c2,c3)][1] >= 12:
                        found = True
                        pos = (c1,c2,c3)
                        rot = r                                #return ((c1,c2,c3),r)
                else:
                    possible_bases[(c1,c2,c3)]= [[s1],1,r]
    #print(possible_bases[(c1,c2,c3)][2])
    #[print(transform(s,[(c1,c2,c3),possible_bases[(c1,c2,c3)][2]])) for s in scanner2]
    new_scanner = scanner2
    if found:
        new_scanner = []
        #print('AAAA')
        #print(pos)
        #print(rot)
        for s2 in scanner2:
            s2 = transform(s2,[pos,rot])
            new_scanner.append(s2)
        #print("BBB")
        #print(scanner2)
        #print(new_scanner)
        #print("CCC")
    return (new_scanner,pos)


def transform(s,b) -> list:
    ns = [0,0,0]
    if b[1][0] < 0:
        ns[0] = -s[abs(-b[1][0])-1]+b[0][0]
    else:
        ns[0] = s[b[1][0]-1]+b[0][0]
    if b[1][1] < 0:
        ns[1] = -s[abs(-b[1][1])-1]+b[0][1]
    else:
        ns[1] = s[b[1][1]-1]+b[0][1]
    if b[1][2] < 0:
        ns[2] = -s[abs(-b[1][2])-1]+b[0][2]
    else:
        ns[2] = s[b[1][2]-1]+b[0][2]

    return ns
def get_rotations() -> list:
    rotations = list()
    base = [1,2,3]
    for x in range(4):
        new_base = base
        if x==1:
            new_base = [-new_base[1],new_base[0],new_base[2]]
        elif x == 2:
            new_base = [-new_base[0],-new_base[1],new_base[2]]
        elif x == 3:
            new_base = [new_base[1],-new_base[0],new_base[2]]
        for y in range(2):
            for z in range(4):
                if y == 0:
                    if z == 1:
                        new_base = [new_base[2],new_base[1],-new_base[0]]
                    elif z == 2:
                        new_base = [-new_base[0],new_base[1],-new_base[2]]
                    elif z == 3:
                        new_base = [-new_base[2],new_base[1],new_base[0]]
                if y == 1:
                    if z == 1:
                        new_base = [new_base[0],new_base[2],-new_base[1]]
                    elif z == 2:
                        new_base = [new_base[0],-new_base[1],-new_base[2]]
                    elif z == 3:
                        new_base = [new_base[0],-new_base[2],new_base[1]]


                if new_base not in rotations:
                    rotations.append(new_base)
    return rotations

global rotations 
rotations = get_rotations()
if __name__=='__main__':
    start = timer()
    scanners = list()
    with open('inputs/day19.txt','r') as f:
        report = f.read().split('\n\n')
    for index,scanner in enumerate(report):
        scanners.append([list(map(int,x.split(','))) for x in scanner.split('\n')[1:]])
    scanners.pop()

    known_scanner = [0]
    beacons = list()
    new_scan = True
    positions = []
    while len(known_scanner)!=len(scanners):
        new_scan = False
        for j,s1 in enumerate(scanners):
            if j not in known_scanner:
                continue
            for i,s2 in enumerate(scanners[1:]):
                i+=1
                if i in known_scanner or j==i:
                    continue
                (scanners[i],pos) = search_base(s1,s2)
                if pos:
                    known_scanner.append(i)
                    positions.append(pos)
    for j,s1 in enumerate(scanners):
        for i,s2 in enumerate(scanners[1:]):
            i+=1
            if j==i:
                continue
            (_,pos) = search_base(s1,s2)
            if pos:
                known_scanner.append(i)
        #if base != ([],[]):
        #    base_transform[i+1] = base
    #print(beacons)
    #print(len(beacons))
    #print(known_scanner)
    res = []
    for i in scanners:
        for s in i:
            if s not in res:
                res.append(s)
    print(len(res))
    maxd = 0
    for p1 in positions:
        for p2 in positions:
            aux = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])
            if aux > maxd:
                maxd = aux

    print(maxd)
