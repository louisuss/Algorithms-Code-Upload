# 부모 찾기 
def find(parent, x):
    if x == parent[x]:
        return x
    else:
        p = find(parent, parent[x])
        parent[x] = p
        return parent[x]

# 부모 합치기 
def union_parent(parent, a, b):
    a = find(parent, a) # a 부모
    b = find(parent, b) # b 부모
    if a != b:
        parent[b] = a # b 부모 -> a
        number[a] += number[b]

t = int(input())

for _ in range(t):
    f = int(input())
    parent = dict()
    number = dict()

    for _ in range(f):
        a, b = input().split()
        # 입력값 부모 존재 여부 확인 후 초기화 
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        # 부모 합 치기 
        union_parent(parent, a, b)
        # 부모 네트워크수 출력 
        print(number[find(parent, a)])



# 연결 리스트로 처리하려면 복잡
# for _ in range(t):
#     f = int(input())
#     network = defaultdict(list);
#     for _ in range(f):
#         a, b = input().split()
#         network[a].append(b)
#         network[b].append(a)
#         print(len(network[a])+1)


