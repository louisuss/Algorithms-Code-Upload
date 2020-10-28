from collections import Counter
# O(n**2)


def min_window(s, t):
    def contains(s_substr_lst, t_lst):
        # t에 있는 문자 체크
        for t_elem in t_lst:
            if t_elem in s_substr_lst:
                s_substr_lst.remove(t_elem)
            else:
                return False
        return True

    if not s or not t:
        return ''

    window_size = len(t)

    # 윈도우 사이즈 늘려가며 반복
    for size in range(window_size, len(s)+1):
        for left in range(len(s) - size + 1):
            # 윈도우 크기의 부분 문자열
            s_substr = s[left:left+size]
            if contains(list(s_substr), list(t)):
                return s_substr
    return ''

# O(n) -> two pointer


def min_window_twopointer(s, t):
    # t 요소 개수
    need = Counter(t)
    # t 개수
    missing = len(t)
    left = start = end = 0

    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        # char이 need에 있으면 값 줄이기
        missing -= need[char] > 0
        need[char] -= 1

        # 필요 문자가 0이면 왼쪽 포인터 이동 판단
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1

            if not end or right - left <= end - start:
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
    return s[start:end]


def min_window_twopointer_counter(s, t):
    t_count = Counter(t)
    current_count = Counter()

    start = float('-inf')
    end = float('inf')

    left = 0
    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        current_count[char] += 1

        # and 연산 결과로 왼쪽 포인터 이동 판단
        while current_count & t_count == t_count:
            if right - left < end - start:
                start, end = left, right
            current_count[s[left]] -= 1
            left += 1
    return s[start:end] if end - start <= len(s) else ''
