def solution(emergency):
    answer=[]
    emergency1=sorted(emergency)
    emergency1.reverse()
    for i in emergency:
        answer.append(emergency1.index(i)+1)
    return answer

 