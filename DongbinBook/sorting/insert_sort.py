# 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
# 필요할 때만 위치를 바꾸므로 데이터가 거의 정렬됐을 때 효율적
# 두 번째 데이터부터 시작
# O(n**2) ~ O(n)
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr)