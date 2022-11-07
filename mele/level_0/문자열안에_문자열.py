# https://school.programmers.co.kr/learn/courses/30/lessons/120908

# 내 풀이
def solution(str1, str2):
  return 1 if str2 in str1 else 2

# 다른 사람 풀이
def solution(str1, str2):
    for i in range(len(str1)):
        stack = ""
        if str1[i] == str2[0]:
            if i + len(str2) > len(str1):
                return 2
            stack += str1[i:i+len(str2)]
            if stack == str2:
                return 1
    return 2
  
def solution(str1, str2):
    answer = 0
    idx = len(str2)
    for i in range(len(str1)):
        if str1[i:i+idx]==str2:
            return 1
    return 2