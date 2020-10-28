s = input()


def longest_palindrome(s):
    # 팰린드롬 판별 및 투포인터 확장
    def expand(left, right):
        # 0123 4 5 6789
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left+1:right-1]

    # 해당 사항이 없을 때 빠른 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s)-1):
        # (i,i+1) - 1,3,5 ... / (i,i+2) - 2,4,6 ...
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result


print(longest_palindrome(s))
