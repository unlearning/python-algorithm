# 공 던지기

# 내 풀이
def solution(numbers, k):
    answer = 2 * (k - 1)
    length = len(numbers) - 1

    while (answer > length):
        length += len(numbers)
        numbers *= 2

    return numbers[answer]

# 내 풀이
def solution(numbers, k):
    return numbers[(2*(k-1))%len(numbers)]


# 다른 사람 풀이
def solution(numbers, k):
    return 2 * (k - 1) % numbers[-1] + 1 # 1부터 순차적으로 증가하기 때문

# 다른 사람 풀이
from collections import deque
def solution(numbers, k):
    array = deque(numbers)

    array.rotate(-(k-1)*2)

    return array[0]