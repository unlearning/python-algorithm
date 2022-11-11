# 나의 풀이
import math

def solution(n):
    answer=math.gcd(6,n)
    return ((6//answer)*(n//answer)*answer)//6

    
    