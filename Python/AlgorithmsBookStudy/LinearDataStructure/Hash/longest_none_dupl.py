def longest_none_duplicate(s):
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 'start' 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        # 현재 문자 위치 삽입
        used[char] = index
    return max_length
