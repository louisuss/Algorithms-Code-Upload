n = int(input())
stores_items = list(map(int, input().split()))
m = int(input())
customer_want = list(map(int, input().split()))


def binary_search(stores_items, start, end, target):
    if start > end:
        return False

    mid = (start+end)//2
    if stores_items[mid] == target:
        return True
    elif stores_items[mid] > target:
        return binary_search(stores_items, start, mid-1, target)
    else:
        return binary_search(stores_items, mid+1, end, target)

    # while start <= end:
    #     mid = (start + end) // 2
    #     if stores_items[mid] == target:
    #         return True
    #     elif stores_items[mid] > target:
    #         end = mid-1
    #     else:
    #         start = mid+1
    # return False


stores_items.sort()
for item in customer_want:
    answer = "yes" if binary_search(
        stores_items, 0, len(stores_items)-1, item) else "no"
    print(answer, end=' ')


# 계수 정렬
arr = [0] * 1000001

for i in stores_items:
    arr[i] = 1

for i in customer_want:
    if arr[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# set 활용
arr2 = set(stores_items)

for i in customer_want:
    if i in arr2:
        print('yes', end=' ')
    else:
        print('no', end=' ')
