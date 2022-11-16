def solution(keyinput, board):
    x=0
    y=0
    answer = [x,y]
    
    for i in keyinput:
      if i=="left":
        x=x-1
      elif i=="right":
        x=x+1
      elif i=="up":
        y=y+1
      elif i=="down":
        y=y-1
      
      # if a in board < x:

      # return answer
    

    return answer