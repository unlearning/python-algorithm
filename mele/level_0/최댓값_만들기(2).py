# https://school.programmers.co.kr/learn/courses/30/lessons/120862

# 내 풀이
def solution(numbers):
    numbers.sort()
    return max(numbers[-1] * numbers[-2], numbers[0] * numbers[1])
  
# TODO: 런타임 에러 발생 이유 연구
def solution(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    min1 = min(numbers)
    numbers.remove(min1)
    max2 = max(numbers)
    min2 = min(numbers)
    return max(max1 * max2, min1 * min2)