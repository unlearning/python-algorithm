# 가위 바위 보

# 첫 번째 내 풀이
def solution(rsp):
    answer = ["0" if i == "2" else "2" if i != "0" else "5" for i in rsp]
    print(type(answer))
    result = "".join(answer)
    return result

# 다른 사람 풀이
def solution(rsp):
    rsp = rsp.replace('2', 's')
    rsp = rsp.replace('5', 'p')
    rsp = rsp.replace('0', 'r')
    rsp = rsp.replace('r', '5')
    rsp = rsp.replace('s', '0')
    rsp = rsp.replace('p', '2')
    return rsp
