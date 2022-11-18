# 1.
def solution(s):
    answer = ''
    for i in s:
        if s.count(i) == 1 and i not in answer:
            answer += i
        else:
            ''
    return ''.join(sorted(answer))
            

# 2.
# for문 안에 if문을 작성했을 시에, 무조건 처음 등장하는 문자만 출력
# → list comprehension
def solution(s):
    answer = "".join(sorted([ch for ch in s if s.count(ch) == 1])) # for과 if문을 동시에
    return answer