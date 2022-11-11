# https://school.programmers.co.kr/learn/courses/30/lessons/120844

# 내 풀이
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == "right" else numbers[1:] + [numbers[0]]

# 다른 사람 풀이
from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

from collections import deque
def solution(numbers, direction):
    queue = deque(numbers)
    if direction == 'right':
        queue.appendleft(queue.pop())
        return list(queue)
    queue.append(queue.popleft())
    return list(queue)

def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0,numbers.pop())
    else:
        numbers.append(numbers.pop(0))
    return numbers
