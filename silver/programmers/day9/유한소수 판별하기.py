# 1.
# keypoint
# 1) math.gcd() : 최대공약수

import math

def solution(a, b):
    # 분자/분모의 최대공약수 구하기
    a_b = math.gcd(a, b)

    # 분자를 최대공약수로 약분
    a = a // a_b

    # 분모를 최대공약수로 약분
    b = b // a_b

    if (b % 2 == 0 or b % 5 == 0) or (a % b == 0): # 분자의 소인수가 2 or 5만 있다는 것을 어떻게 확인?
        return 1
    else:
        return 2