# n의 배수 고르기

# 첫 번째 내 풀이
def solution(n, numlist):
    answer = []

    for i in numlist:
        if i % n == 0:
            answer.append(i)

    return answer

# 두 번째 내 풀이
def solution(n, numlist):
    return list(filter(lambda x: x % n == 0 , numlist))


# 다른 사람 풀이
def solution(n, numlist):
    return [num for num in numlist if num % n == 0]
