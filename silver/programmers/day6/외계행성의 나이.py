# 1.
def solution(age):
    answer = {
        0:'a', 1:'b', 2:'c',
        3:'d', 4:'e', 5:'f',
        6:'g', 7:'h', 8:'i',
        9:'j'
    }
    return ''.join(map(str, [answer[int(x)] for x in list(str(age))])) # Q.

# 2.
def solution(age):
    str_age = str(age)
    answer = ''
    lst =["a","b","c","d","e","f","g","h","i","j"]
    for ch in str_age:
        for i in range(0,10):
            if int(ch) == i:
                answer += lst[i]
    return answer
