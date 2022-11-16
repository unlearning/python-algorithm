def solution(n):
  a=2
  answer = []
  while a<= n:
      if n%a == 0:
          n=n/a
          if a not in answer:
            answer.append(a)
      else:
          a=a+1
  return answer
print(solution(12))
