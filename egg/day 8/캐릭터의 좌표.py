# 캐릭터의 좌표

# 내 풀이
def solution(keyinput, board):
    answer = {
        "up"    :[0, 1],
        "down"  :[0, -1],
        "left"  :[-1, 0],
        "right" :[1, 0]
    }
    result = []
    fnum = 0
    snum = 0

    for i in keyinput:
        if abs(fnum)<=board[0]/2:
            fnum += answer[i][0]
            if abs(fnum) > board[0]/2:
                fnum -= answer[i][0]
        
        if abs(snum) <= board[1]/2:
            snum += answer[i][1]
            if abs(snum) > board[1]/2:
                snum -= answer[i][1]
    
    result.append(fnum)
    result.append(snum)
    return result


# 다른 사람 풀이
def solution(keyinput, board):
    x_lim, y_lim = board[0]//2, board[1]//2
    move = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    x, y = 0, 0
    for k in keyinput:
        dx, dy = move[k]
        if abs(x+dx) > x_lim or abs(y+dy) > y_lim:
            continue
        else:
            x, y = x+dx, y+dy

    return [x, y]

# 다른 사람 풀이
from functools import reduce

def solution(keyinput, board):
    move = {"left": [-1, 0], "right": [1, 0], "up": [0, 1], "down": [0, -1]}
    return reduce(lambda pos, key: [p+m if -(b//2) <= p+m <= b//2 else p for p, m, b in zip(pos, move[key], board)], keyinput, [0,0])