# 1.
def solution(n):
    pizza = 6
    while(pizza % n != 0):
        pizza += 6
    return pizza // 6

# 2.
# 최대공약수 풀이