# 1.
def solution(numbers):
    numbers = sorted(numbers)
    print(numbers)

    if numbers[0] and numbers[1] < 0:
        if numbers[-1] * numbers[-2] > numbers[0] * numbers[1]: # [-1, 7, 1, -6]일 경우
           return numbers[-1] * numbers[-2]
        else:
            return numbers[0] * numbers[1]
    else:
        return numbers[-1] * numbers[-2]

# 2.
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2]) 
