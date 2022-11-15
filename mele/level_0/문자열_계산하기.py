# https://school.programmers.co.kr/learn/courses/30/lessons/120902

# 내 풀이
def solution(my_string):
    return eval(my_string)

# 다른 사람 풀이
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

def solution(my_string):
    s = my_string.split()
    answer = int(s[0])
    for i in range(1,len(s),2):
        if s[i]=='+':
            answer+=int(s[i+1])
        else:
            answer-=int(s[i+1])
    return answer
