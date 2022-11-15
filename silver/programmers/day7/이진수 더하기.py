# 1.
def solution(bin1, bin2):
    i_bin1 = int(bin1, 2)
    i_bin2 = int(bin2, 2)
    answer = i_bin1 + i_bin2
    return bin(answer)[2:]

# 2.
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer