# 1.
def solution(my_string):
    return eval(my_string)

# 2.
solution = eval

# 3.
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))