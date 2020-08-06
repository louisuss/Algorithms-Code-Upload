
def solution(s):
    # substring길이: 길이 ~ 1
    for i in range(len(s), 0, -1):
        # 시작점
        for j in range(len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                return i

# # DP 활용
# def solution(s):
#     longest_palindrome = 0
#     n = len(s)
#     table = [[False]*n for _ in range(n)]

#     # 다음과 같은 방식으로 테이블을 만든다:
#     for i in range(n):
#         for j in range(n-i):
#             # len(substring) < 3 일 경우(다르게 표현하면, 두번째 대각선 줄을 만들 때까지)
#             # substring의 끝이 같을 경우 True를 넣고, longest_palindrome 을 업데이트 한다
#             if i < 2:
#                 if s[j] == s[i+j]:
#                     table[j][i+j] = True
#                     longest_palindrome = i+1
#                 else:
#                     table[j][i+j] = False
#             # len(substring) > 3 일 경우
#             # substring의 끝이 같고, 왼쪽 밑 대각선 한칸에 있는 박스가 True면 True를 넣고, longest_palindrome을 업데이트 한다.
#             else:
#                 if s[j] == s[i+j] and table[j+1][i+j-1]:
#                     table[j][i+j] = True
#                     longest_palindrome = i+1
#                 else:
#                     table[j][i+j] = False
#     return longest_palindrome
