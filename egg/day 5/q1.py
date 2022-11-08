# 아이스 아메리카노
def solution(money):
    answer = [0, 0]
    answer[0] = money // 5500
    answer[1] = int(money % 5500)
    return answer


# 피자 나눠 먹기(3)
def solution(slice, n):
    return (n-1)//slice + 1


# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

# 배열 두배 만들기


def solution(numbers):
    answer = [num * 2 for num in numbers]
    return answer

# 배열 원소의 길이


def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))

    return answer


# 짝수는 싫어요
def solution(n):
    answer = [num for num in range(1, n+1, 2)]
    return answer


# 최댓값 만들기
def solution(numbers):
    numbers.sort()
    fnum = numbers.pop(len(numbers)-1)
    snum = numbers.pop(len(numbers)-1)
    answer = fnum * snum
    return answer

# def solution(numbers):
#     max1 = max(numbers)
#     numbers.remove(max1)
#     return max1*max(numbers)


# 옷 가게 할인 받기
def solution(price):
    answer = 0

    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else:
        answer = price

    return int(answer)


# 점의 위치 구하기
def solution(dot):
    answer = 0

    if dot[0] < 0:
        if dot[1] < 0:
            answer = 3
        else:
            answer = 2
    else:
        if dot[1] < 0:
            answer = 4
        else:
            answer = 1

    return answer


# 문자열 안에 문자열
def solution(str1, str2):

    if str2 in str1:
        return 1
    else:
        return 2


# 제곱수 판별하기
def solution(n):
    result = 0
    for i in range(1, 1001):
        result = i ** 2
        if result == n:
            return 1

    return 2


# 문자 반복 출력하기
def solution(my_string, n):
    answer = list(my_string)
    for i in range(len(my_string)):
        answer[i] = answer[i] * n

    return "".join(answer)


# 특정 문자 제거하기
def solution(my_string, letter):
    rlist = my_string.count(letter)

    for i in range(rlist):
        my_string = my_string.replace(letter, "")

    return my_string


# 삼각형의 완성조건
def solution(sides):
    fnum = max(sides)
    sides.remove(fnum)

    total = sum(sides)

    if fnum < total:
        return 1
    else:
        return 2


# 배열의 유사도
def solution(s1, s2):
    answer = 0

    for i in s1:
        if i in s2:
            answer += 1
    return answer


# 순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer


# 자릿수 더하기
def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)):
        answer.append(n[i])

    total = sum(answer)
    return total


# 세균 증식
def solution(n, t):
    answer = n * 2**t
    return answer


# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        asc = ord(my_string[i])
        if asc >= 48 and asc <= 57:
            answer.append(int(my_string[i]))
    return sum(answer)

# isdigit() 함수를 사용해서 풀기

# 모음 제거


def solution(c):
    answer = c
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in c.lower():
        if x in vowels:
            answer = answer.replace(x, "")

    return answer


# 개미 군단
def solution(hp):
    ant1 = divmod(hp, 5)
    if ant1[1] == 0:
        return ant1[0]
    else:
        ant2 = divmod(ant1[1], 3)
        if ant2[1] == 0:
            return ant1[0] + ant2[0]
        else:
            ant3 = divmod(ant2[1], 1)
            return ant1[0] + ant2[0] + ant3[0]
