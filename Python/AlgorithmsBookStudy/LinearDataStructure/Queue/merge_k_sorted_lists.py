import heapq

lst = [[1, 4, 5], [1, 3, 4], [2, 6]]


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


merge_list(lst)
