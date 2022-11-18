# 유한소수 판별하기

# 내 풀이
import math

def solution(a, b):
    answers = []
    answer = math.gcd(a, b)
    fnum = b
    b = b//answer
    result = 1

    # 최대공약수로 나눈 분모를 소인수분해
    for i in range(2, b + 1):
        if i % int(i**0.5) != 0 or i == 2 or i == 3:
            while fnum % i == 0:
                answers.append(i)
                fnum = fnum // i

    # 소인수분해한 분모에 2, 5가 아닌 숫자가 들어가면 2리턴
    for l in answers:
        if l == 2 or l == 5:
            pass
        else:
            return 2

    return result

# 다른 사람 풀이
def solution(a, b):
    
    return 1 if a/b * 1000 % 1 == 0 else 2