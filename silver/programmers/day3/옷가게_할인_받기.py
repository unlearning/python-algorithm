# 1.
def solution(price):
    if price >= 500000:
        price -= price * 0.2
        return int(price)
    elif price >= 300000:
        price -= price * 0.1
        return int(price)
    elif price >= 100000:
        price -= price * 0.05
        return int(price)
    else:
        return int(price)

# 2.
def solution(price):
    if price>=500000: # 왜 거꾸로 진행하면 안될까?
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)