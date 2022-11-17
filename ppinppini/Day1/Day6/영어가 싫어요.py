def solution(numbers):
  answer=''
  answer1=''
  dic={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
  for i in numbers:
      answer+=i
      if   answer in list(dic.keys()):
        answer1+=dic.get(answer)
        answer=''
  return int(answer1)
      
      



