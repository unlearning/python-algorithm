def solution(numbers,k):
  answer=0
  for _ in range(1,k):
    answer=answer+2
    answer=answer%len(numbers)
  return numbers[answer]