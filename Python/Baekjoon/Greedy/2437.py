# 1 1
# 2 2
# 3 3
# 4 1 3
# 5 2 3
# 6 6 -> S (이전상태까지 만들수있는 무게)
# 7 7
# 8 1 7
# 9 3 6
# 13 6 7
# 1부터 6까지 만들 수 있으면 7~13까지도 만들수 있음
# 1~6 +7 = 7~13
# 기존수 + 1에 해당하는 수가 없으면 그 수가 최소
# sum[i] + 1 의 값이 s[i + 1]의 값보다 크다면 sum[i] + 1을 출력해준다.

# N, A = int(input()), sorted(list(map(int, input().split())))

# ans = 0
# # i ans+1 ans
# # 1 0+1=1 1
# # 1 1+1=2 1+1=2
# # 2 2+1=3 2+2=4
# # 3 4+1=5 4+3=7
# # 6 7+1=8 7+6=13
# # 7 13+1=14 13+7=20
# # 30 20+1=21

# for i in A:
#     if i <= ans + 1:
#         ans += i
#     else:
#         break
# print(ans+1)

# n = int(input())
# s = sorted(list(map(int, input().split())))
# num = 1
# for i in range(n):
#     if num < s[i]:
#         break
#     num += s[i]
# print(num)
