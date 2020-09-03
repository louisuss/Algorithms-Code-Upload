n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = 0

# 가장 큰수와 다음으로 큰수가 같은 경우
if arr[-1] == arr[-2]:
    result += arr[-1]*m
else:
    # 중복 가능 횟수가 더 큰 경우
    if k >= m:
        result += arr[-1]*m
    else:
        count = m//(k+1)
        count_left = m % (k+1)
        result += (count)*k*arr[-1] + (count)*arr[-2] + count_left * arr[-1]

        # while m:
        #     if m-k >= 0:
        #         result += arr[-1]*k
        #         m -= k
        #     else:
        #         result += arr[-1]*m
        #         m -= m
        #     if m-1 >= 0:
        #         result += arr[-2]
        #         m -= 1
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += arr[-1]
#         m -= 1
#     if m == 0:
#         break
#     result += arr[-2]
#     m -= 1

print(result)
