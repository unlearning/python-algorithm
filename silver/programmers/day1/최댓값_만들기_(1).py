# 1.
def solution(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 * max2

# 2. 
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]