strs = input()
result = 0


def LongestSubstring(s):
    used = {}
    print(type(used))
    max_length = start = 0
    for index, char in enumerate(s):
        # 중복된 문자 등장 시 'start' 위치 갱신 - 중복문자 생긴 다음 인덱스
        if char in used and start <= used[char]:
            start = used[char] + 1
        # 중복 아닌 경우, 최대 길이 갱신
        else:
            # 길이는 +1 해야됨
            max_length = max(max_length, index - start + 1)
        # 해당 문자가 사용된 인덱스 저장
        used[char] = index
    return max_length


for i in range(len(strs)):
    temp = ''
    for j in range(i, len(strs)):
        if strs[j] in list(temp):
            break
        temp += strs[j]
    result = max(result, len(temp))

print(LongestSubstring(strs))
print(result)
