
def solution(my_str,n):
    
    answer= []
    for i in range(0,len(my_str),n):
      k=i+n
      answer.append(my_str[i:k])
    return answer

    
      