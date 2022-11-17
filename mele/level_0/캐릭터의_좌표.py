# https://school.programmers.co.kr/learn/courses/30/lessons/120861

# 내 풀이
def solution(keyinput, board):
    location = [0, 0]
    command = {
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        'right': [1, 0]
    }
    for key in keyinput:
        location[0] += command[key][0]
        location[1] += command[key][1]
        if abs(location[0]) > board[0]//2:
            location[0] -= command[key][0]
        if abs(location[1]) > board[1]//2:
            location[1] -= command[key][1]
    return location

# 다른 사람 풀이
def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy
    return [x,y]

from functools import reduce
def solution(keyinput, board):
    move = {"left": [-1, 0], "right": [1, 0], "up": [0, 1], "down": [0, -1]}
    return reduce(lambda pos, key: [p+m if -(b//2) <= p+m <= b//2 else p for p, m, b in zip(pos, move[key], board)], keyinput, [0,0])