# https://school.programmers.co.kr/learn/courses/30/lessons/120860

# 내 풀이
def solution(dots):
    max_x = max(dot[0] for dot in dots)
    min_x = min(dot[0] for dot in dots)
    max_y = max(dot[1] for dot in dots)    
    min_y = min(dot[1] for dot in dots)    
    return (max_x - min_x) * (max_y - min_y)

# 다른 사람 풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])