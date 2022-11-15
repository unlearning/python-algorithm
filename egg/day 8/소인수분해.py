# 소인수분해

# 내 풀이
def solution(n):
    answer = []
    k = n
    for i in range(2, n + 1):
        if i % int(i**0.5) != 0 or i == 2 or i == 3:
            while k % i == 0:
                answer.append(i)
                k = k // i

    return sorted(set(answer))

# 다른 사람 풀이
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
