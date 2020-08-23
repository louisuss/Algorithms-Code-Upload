from collections import defaultdict
# 에러

# 1. 루트 노드 존재 여부 및 루트 노드가 유일한지 확인
# 2. 진입 차수가 1
# 3. 엣지 + 1 = 노드수

lst = []
while True:
    temp = list(map(int, input().split()))
    if temp:
        if temp[-1] == -1 and temp[-2] == -1:
            break
        else:
            lst.extend(temp)

temp = defaultdict(list)
temp_node = set()
cases = []
node_cnt = []
for i in range(0, len(lst), 2):
    if lst[i] == 0 and lst[i+1] == 0:
        cases.append(temp)
        node_cnt.append(temp_node)
        temp = defaultdict(list)
        temp_node = set()
    else:
        temp_node.add(lst[i])
        temp_node.add(lst[i+1])
        temp[lst[i+1]].append(lst[i])

for i, case in enumerate(cases, 1):
    s = set()
    check = True
    node = len(node_cnt[i-1])
    edge_cnt = 0

    for val in case.values():
        # 2번조건 - 들어오는 간선이 여러개인 경우
        if len(val) > 1:
            check = False
        # # 루트 노드 개수 체크
        for v in val:
            edge_cnt += 1
            if v not in case.keys():
                s.add(v)

    # 1번 조건
    if len(s) != 1:
        check = False

    # 3번 조건
    if (node - 1) != edge_cnt:
        check = False

    if check:
        print("Case {} is a tree.".format(i))
    else:
        print("Case {} is not a tree.".format(i))
