def solution(s):
    answer = ''
    
    for i in s:
      if s.count(i)==1:
        answer=answer+i
    answer2=''.join(sorted(answer))   
    return answer2