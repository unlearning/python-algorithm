# bin1="0b10"
# bin2="0b11"

# print((int(bin1,2))+(int(bin2,2)))

# # # 나의 풀이
def solution(bin1,bin2):
    answer= (int(bin1,2))+(int(bin2,2))
    return bin(answer).replace("0b","")




