def ascending(arr):
    now = arr[0]
    result = 1
    for i in range(1, len(arr)):
        if now < arr[i]:
            result += 1
            now = arr[i]
    return result
n = input()
arr = []
for _ in range(n):
    arr.append(int(input()))

print(ascending(arr))
arr.reverse()
print(ascending(arr))

# t = int(input())
# t_list = []
# for _ in range(t):
#     t_list.append(int(input()))
#
# min = t_list[0]
# cnt1 = 1
# cnt2 = 1
# for i in range(1, len(t_list)):
#     if min < t_list[i]:
#         cnt1 += 1
#         min = t_list[i]
#
# min2  = t_list[-1]
# for i in range(len(t_list)-1, -1, -1):
#     if min2 < t_list[i]:
#         cnt2 += 1
#         min2 = t_list[i]
#
# print(cnt1)
# print(cnt2)


