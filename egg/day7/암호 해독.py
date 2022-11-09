# 암호 해독

# 첫 번째 내 풀이
def solution(cipher, code):
    answer = [cipher[i] for i in range(len(cipher)) if i % code == code-1]
    return "".join(answer)

# 두 번째 내 풀이
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

# 다른 사람 풀이
def solution(cipher, code):
    answer = ''
    index = list(range(code, len(cipher)+1, code))
    for i in index:
        answer += cipher[i-1]
    return answer
