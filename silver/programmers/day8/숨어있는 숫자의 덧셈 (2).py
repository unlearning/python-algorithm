# 1.
# re.sub('[^0-9]', '', my_string) : 숫자가 아닌('[^0-9]) 문자들을 제거('')
import re

def solution(my_string):
    answer = re.findall(r'\d+', my_string) # r'\d+' : 연속된 숫자들의 패턴, re.findall(pattern, string): 패턴들을 리스트로 반환
    return sum([int(i) for i in answer])

# 2.
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    # print(s) :    1 2  34 
    return sum(int(i) for i in s.split())

print(solution("aAb1B2cC34oOp"))