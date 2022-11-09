# https://school.programmers.co.kr/learn/courses/30/lessons/120845

# 내 풀이
def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)

# 다른 사람 풀이
import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box)) # 요소 전체를 곱해주는 함수