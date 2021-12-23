import numpy as np

mv = {'A':1,'B':10,'C':100,'D':1000}

def print_board(gb):
    print()
    [print(str(i)+' '+' '.join(x)) for i,x in enumerate(gb)]
    print('  '+'0 1 2 3 4 5 6 7 8 9 0 1 2')
    print()
    return

def move(gameboard):
    print('Select a piece:')
    pos = list(map(int,input().split(',')))
    print('Select dest:')
    des = list(map(int,input().split(',')))
    cost = (abs(pos[0]-des[0])+abs(pos[1]-des[1]))*mv[gameboard[pos[0],pos[1]]]
    gameboard[des[0],des[1]] = gameboard[pos[0],pos[1]]
    gameboard[pos[0],pos[1]] = '.'
    return cost


if __name__=='__main__':
    print('Select game (1 or 2):')
    sel = input()
    if sel == '1':
        gameboard = np.full((5,13),'#')
        gameboard[1,1:-1] = '.'
        with open('inputs/day23.txt','r') as f:
            inputs = f.readlines()
            gameboard[2,[3,5,7,9]] = [inputs[2][3],inputs[2][5],inputs[2][7],inputs[2][9]]
            gameboard[3,[3,5,7,9]] = [inputs[3][3],inputs[3][5],inputs[3][7],inputs[3][9]]
        cost = 0
        while True:
            print_board(gameboard)
            cost += move(gameboard)
            print(f'\nCost: {cost}')
    elif sel == '2':
        gameboard = np.full((7,13),'#')
        gameboard[1,1:-1] = '.'
        with open('inputs/day23.txt','r') as f:
            inputs = f.readlines()
            gameboard[2,[3,5,7,9]] = [inputs[2][3],inputs[2][5],inputs[2][7],inputs[2][9]]
            gameboard[3,[3,5,7,9]] = ['D','C','B','A']
            gameboard[4,[3,5,7,9]] = ['D','B','A','C']
            gameboard[5,[3,5,7,9]] = [inputs[3][3],inputs[3][5],inputs[3][7],inputs[3][9]]
        cost = 0
        while True:
            print_board(gameboard)
            cost += move(gameboard)
            print(f'\nCost: {cost}')
        
    else:
        print('Invalid game')
