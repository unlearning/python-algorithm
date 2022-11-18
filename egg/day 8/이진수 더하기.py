# 이진수 더하기

# 내 풀이
def solution(bin1, bin2):
    answer = int('0b' + bin1,2)
    answer2 = int('0b' + bin2,2)
    

    return bin(answer + answer2)[2:]

print(solution("10", "11"))