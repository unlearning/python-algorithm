# 1.
# 각각의 for문 내 변수 i는 해당 반복문 내에서만 쓰이기 때문에, 중복되어도 상관 x
# return은 한 번만

def solution(balls, share):
    n = 1
    for i in range(1, balls + 1):
        n *= i

    n_m = 1
    for i in range(1, balls - share + 1, 1): # balls - share에도 +1 할 것
        n_m *= i

    m = 1
    for i in range(1, share + 1):
        m *= i
    
    return n // (n_m * m)

# 1-1.
import math

def solution(balls, share):
    n_answer = math.factorial(balls)
    m_answer = math.factorial(share)
    n_m = math.factorial(balls - share)
    return n_answer // (n_m * m_answer)