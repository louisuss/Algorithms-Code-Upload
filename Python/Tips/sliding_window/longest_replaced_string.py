from collections import Counter


def make_longest_string(s, k):
    left = right = 0
    cnts = Counter()
    for right in range(len(s)):
        cnts[s[right]] += 1
        # 최고 빈번한 값의 횟수
        max_char_n = cnts.most_common(1)[0][1]

        # left는 가능한 안움직이는게 좋지만 k 연산 횟수 넘어가면 이동해야 함
        # if right - left - max_char_n > k:
        # 범위가 가장 빈번한 문자 + 해당 문자로 변경한것보다 큰경우 사이즈 줄여야함
        # 이 연산이 이해하기 더 용이함.
        if right - left > k + max_char_n:
            # left 이동
            cnts[s[left]] -= 1
            left += 1
        # max_len = max(right-left, max_len) 생략 가능
        # 한번 최대값이 된 상태에서 오른쪽 포인터가 한칸이동하면 왼쪽 포인터도 따라서 이동하게 되므로 max_len은 변하지 않음
    return right - left


s = input()
k = int(input())
print(make_longest_string(s, k))
