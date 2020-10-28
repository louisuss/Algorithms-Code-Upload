from copy import deepcopy

n = int(input())
n_set = set(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

for v in m_list:
    if v not in n_set:
        print(0)
    else:
        print(1)

# for v in m_list:
#     temp = deepcopy(n_set)
#     temp.add(v)
#     if temp == n_set:
#         print(1)
#     else:
#         print(0)
