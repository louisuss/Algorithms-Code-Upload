def longestPalindrome(s):
    def expand(left, right):
        # 제한 범위 / 왼쪽 오른쪽 같은 경우
        # 슬라이싱 조회 vs 인덱스 조회
        # s = '12345' / s[1:3] = 23 / s[3] = 4
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            print(left,right)
            left -= 1
            right += 1
        # 마지막 추가된 부분 빼주고 더해줘야됨
        return s[left+1:right-1]

    # 초기 조건
    if len(s) < 2 or s == s[::-1]:
        return s
    result = ''

    # 0부터 슬라이싱
    for i in range(len(s)-1):
        # i, i+1 -> 짝수 / i, i+2 -> 홀수
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result


user_input = input()
print(longestPalindrome(user_input))
