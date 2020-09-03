n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)

for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break
print(sum(arr1))

# 배열1에서 가장 작은 원소가 배열2에서 가장 큰 원소보다 작을 때교체
# while k > 0:
#     min_idx = arr1.index(min(arr1))
#     max_idx = arr2.index(max(arr2))

#     if min(arr1) < max(arr2):
#         arr1[min_idx], arr2[max_idx] = arr2[max_idx], arr1[min_idx]
#     else:
#         break
#     k -= 1
