# 1.
def solution(numbers, direction):
    return numbers[-1:] + numbers[0:-1] if direction == "right" else numbers[1:] + numbers[0:1]

# 2.
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
