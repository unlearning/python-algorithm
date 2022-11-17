# 삼각형의 완성조건(2)

# 내 풀이
def solution(sides):
    fnum, snum = sides[0] , sides[1]
    return (fnum + snum) - abs(fnum - snum) -1

# 다른 사람 풀이
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

# 다른 사람 풀이
def solution(sides):
    return len(list(range(abs(sides[0]-sides[1])+1,sum(sides))))