# 1.
def solution(numbers, k):
    numbers = numbers * k
    answer = numbers[k * 2 - 2] 
    return answer

# 2.
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]