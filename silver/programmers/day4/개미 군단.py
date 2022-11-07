# 1.
def solution(hp):
    total = hp // 5
    bi = hp % 5
    total += bi // 3 + bi % 3
    return total

# 2.
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
