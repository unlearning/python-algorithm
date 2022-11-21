def solution(array):
  answer=[]
  result=[]
  answer1=[]
  for i in array:
      answer.append(sum(i))
      
      
  result=sorted(answer,reverse=True)   
  for j in answer:
    answer1.append(result.index(j)+1)
  return answer1 
