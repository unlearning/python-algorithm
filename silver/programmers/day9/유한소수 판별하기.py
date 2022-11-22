# 1.
# keypoint
# 1) math.gcd() : 최대공약수

import math

def solution(a, b):
    b //= math.gcd(a,b) # 분자, 분모의 최대공약수로 분모를 약분하여 기약분수로 만들기
    while b % 2 == 0: # 1) 분모가 2로 나눠질 때까지 
        b //= 2 # 2로 나누는 과정 반복
    while b % 5 == 0: # 2) 2로 나눌 때까지 나눈 후, 5로 나눠질 때까지
        b //= 5 # 5로 나누는 과정 반복
    return 1 if b == 1 else 2 # 분모의 남은 약수가 1이라면 1, 아니라면 2 반환