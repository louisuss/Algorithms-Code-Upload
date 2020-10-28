import heapq
from collections import defaultdict

lst = [[1, 4, 5], [1, 3, 4], [2, 6]]

# heapq 사용
def merge_list(lists):
    result = []
    heap = []
    for idx, lst in enumerate(lists):
        for val in lst:
            heapq.heappush(heap, (val, idx))

    while heap:
        val = heapq.heappop(heap)
        result.append(val[0])

    print('->'.join(map(str, result)))

def merge_list2(lists):
    result = []
    merge_dict = defaultdict(list)

    for lst in lists:
        for val in lst:
            merge_dict[val].append(val)
    
    for item in sorted(merge_dict.values()):
        for val in item:
            result.append(val)
    
    print('->'.join(map(str,result)))


merge_list2(lst)
