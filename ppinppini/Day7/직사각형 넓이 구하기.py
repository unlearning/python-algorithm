# 나의풀이
def solution(dots):
    maxx1 = max(dot[0] for dot in dots)
    minx2 = min(dot[0] for dot in dots)
    maxy1 = max(dot[1] for dot in dots)    
    miny2 = min(dot[1] for dot in dots)    
    return (maxx1 - minx2) * (maxy1 - miny2)

# # 다른사람풀이
# def solution(dots):
#     return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])