# 나의풀이
def solution(numbers,direction):
  from collections import deque
  answer=deque(numbers)
  if direction == "right":
    answer.rotate(1)
  else :
    answer.rotate(-1)
    
  return  list(answer)