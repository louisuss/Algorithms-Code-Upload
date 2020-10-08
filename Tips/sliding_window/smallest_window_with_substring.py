from collections import Counter

s = input()
t = input()

# 슬라이딩 윈도우 크기를 t 길이 부터 증가 시키면서 BF


def get_smallest_sub(s, t):

    # 문자 단위 포함 여부 판별은 반드시 일대일 문자가 대응되어야 함. 한번에 비교 어려움. 정렬해서 풀기도 어려움.
    def contains(sub, t_lst):
        for val in t_lst:
            # 포함 관계 in 확인하기 위해서는 리스트 형태여야 함
            if val in sub:
                sub.remove(val)
            else:
                return False
        return True

    # 예외 케이스
    if not s or not t:
        return ''

    # 윈도우 크기 변경
    for window_size in range(len(t), len(s)+1):
        # 인덱스 위치 변경
        for left in range(len(s)-window_size+1):
            # 부분 문자열
            sub = s[left:left+window_size]
            if contains(list(sub), list(t)):
                return sub
    return ''


# 투포인터, 슬라이딩 윈도우
# 계속 우측으로 이동하는 슬라이딩 윈도우이면서 적절한 위치 찾은 경우 좌우 포인터 크기를 좁혀나가는 투 포인터 풀이
def get_smallest_sub2(s, t):
    # 필요한 문자 각각의 개수
    need = Counter(t)
    # 필요한 문자 전체 개수
    missing = len(t)
    left = start = end = 0

    # right 이동
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1  # 해당 문자가 아닌 경우 음수로 만들게 됨

        # 필요 문자가 0이면 왼쪽 포인터 더 줄일 수 있는지 판단
        if missing == 0:
            while left < right and need[s[left]] != 0:
                need[s[left]] += 1
                left += 1

            # not end = 초기값이 end=0이기 때문, right-left=새로운 값, end-start=기존값
            if not end or (right - left <= end - start):
                # 갱신
                start, end = left, right
                # left 이동
                need[s[left]] += 1
                missing += 1
                left += 1
    return s[start:end]

# Counter 교집합


def get_smallest_sub3(s, t):
    t_cnt = Counter(t)
    cur_cnt = Counter()

    start = float('-inf')
    end = float('inf')
    left = 0

    # right 이동
    for right, char in enumerate(s, 1):
        cur_cnt[char] += 1

        # 필요한 문자 다 찾은 경우
        while cur_cnt & t_cnt == t_cnt:
            # 최소 윈도우 갱신
            if right - left < end - start:
                start, end = left, right
            # left 이동하기 때문에 이동한 후 윈도우에 포함되지 않는 값 제거
            cur_cnt[s[left]] -= 1
            # left 이동
            left += 1


print(get_smallest_sub2(s, t))
