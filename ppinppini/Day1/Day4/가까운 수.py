def solution(array,n):
  array.sort()
  answer=0
  max=100
  for i in array:

    if max>abs(n-i) :
      max=abs(n-i)
      answer=i
  return answer
     