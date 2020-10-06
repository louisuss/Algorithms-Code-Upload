import heapq

a = [2,4,1,2,3,5,7,5]

heapq.heapify(a)
print(heapq.nlargest(4, a)[-1])