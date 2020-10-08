import heapq

# 우선순위 큐 활용


def reconstruct_queue(people):
    result = []
    heap = []
    # 최대힙으로 변경
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))

    while heap:
        person = heapq.heappop(heap)
        # person[1] == index
        result.append(person[1], [-person[0], person[1]])
    return result


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
