# 1.
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        else:
            answer += "2"
    return answer

# 2.
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

# 3.
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp
