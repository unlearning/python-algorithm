# 구슬을 나누는 경우의 수

# 내 풀이
def solution(balls, share):
    answer = 1
    mult = 1

    for i in range(1,share+1):
        answer *= i
        mult *= balls
        balls -= 1

    return mult//answer


# 다른 사람 풀이
import math

def solution(balls, share):
    return math.comb(balls, share)


