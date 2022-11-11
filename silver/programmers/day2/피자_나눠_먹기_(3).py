# 1.
def solution(slice, n):
    if n % slice == 0:
        return n // slice
    else:
        return n // slice + 1
# 2.
def solution(slice, n):
    return ((n - 1) // slice) + 1

# 3.
def solution(slice, n):
    return -(n//slice) # -1.1 -- // --> -2
