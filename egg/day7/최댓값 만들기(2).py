# 최댓값 만들기(2)

# 첫 번째 내 풀이
def solution(numbers):
    numbers.sort()

    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        return numbers[0] * numbers[1]
    else :
        return numbers[-1] * numbers[-2]
        


# 다른 사람 풀이
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2])
