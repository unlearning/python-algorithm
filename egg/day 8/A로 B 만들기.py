# A로 B 만들기

# 내 풀이
def solution(before, after):

    # 문자열은 sort 함수 사용 불가 sorted를 이용
    before = sorted(before)
    after = sorted(after)

    if before == after:
        return 1
    else:
        return 0

print(solution("olleh", "hello"))
