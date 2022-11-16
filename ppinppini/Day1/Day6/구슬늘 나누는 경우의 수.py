def solution(balls,share):
    answer=1
    answer1=1
    for i in range(balls-share+1,balls+1):
      answer=answer*i
    for j in range(1,share+1):
        answer1=answer1*j
    return answer/answer1