# 1.
n = int(input())
i = 0
while True:
    i += 1
    if i > n: break
    print('*' * i)

# 2.
n = int(input())
for i in range(n):
    print('*' * (i + 1))
