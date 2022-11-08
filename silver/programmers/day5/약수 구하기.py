# 1.
def solution(n):
    array = []
    i = 0
    while i <= n:
        i += 1
        if n % i == 0:
            array.append(i)
    return sorted(array)

# 2.
def solution(n):
    answer = []

    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)
            
    return answer
