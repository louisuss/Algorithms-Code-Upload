import bisect


def give_cookie(g, s):
    g.sort()
    s.sort()

    child_i = cookie_i = 0
    # 만족하지 못할 때까지 진행
    while child_i < len(g) and cookie_i < len(s):
        if s[cookie_i] >= g[child_i]:
            child_i += 1
        cookie_i += 1
    return child_i

# 이진 검색
# 하나의 리스트를 순회하면서 다른 하나는 이진 검색
# 찾아낸 인덱스가 현재 부여한 아이들보다 클 경우 더 줄 수있는 경우이기 때문에 아이들 수 증가


def give_cookie2(g, s):
    g.sort()
    s.sort()

    result = 0
    # 쿠키
    for i in s:
        # 이진검색으로 더 큰 인덱스 탐색
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    return result
