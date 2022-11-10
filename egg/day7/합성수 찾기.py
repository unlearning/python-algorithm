# 합성수 찾기

# 첫 번째 내 풀이
def solution(n):
    count = 0

    for i in range(1,n+1):
        answer = sorted(filter(lambda x: i % x == 0, range(1, n+1)))
    
        if len(answer) >= 3:
            count += 1

    return count

# 다른 사람 풀이
def get_divisors(n):
    return list(filter(lambda v: n % v == 0, range(1, n+1)))


def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))

# 다른 사람 풀이
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output
