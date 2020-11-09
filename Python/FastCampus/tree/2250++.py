# level = 행
# width = 해당 레벨 가장 오른쪽 열 - 가장 왼쪽 열 + 1
# 중위 순회 - X축을 기준으로 왼쪽부터 방문
# 중위 순회 알고리즘 이용, level 값 저장

class Node:
    def __init__(self, number, left_node, right_node):
        # parent 유무 체크. parent 없으면 root node. parent 없는 노드부터 순회 진행.
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

# root, 1 부터 시작


def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    # 왼쪽노드 방문
    if node.left_node != -1:
        in_order(tree[node.left_node], level+1)

    # 데이터 처리
    # 현재 레벨 기준으로 레벨의 가장 작은값 찾기. 해당 레벨의 가장 왼쪽 변수 찾기
    level_min[level] = min(level_min[level], x)
    # 현재 레벨 기준으로 레벨의 가장 큰값 찾기. 해당 레벨의 가장 오른쪽 변수 찾기
    level_max[level] = max(level_max[level], x)
    x += 1  # 열 오른쪽으로 한칸 이동

    # 오른쪽 노드 방문
    if node.right_node != -1:
        in_order(tree[node.right_node], level+1)


n = int(input())
tree = {}

# [19, 10, 3, 2, 1, 4, 6, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]
# [0, 10, 15, 19, 18, 16, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
level_min = [n]*(n+1)  # 노드 개수만큼 지정
level_max = [0]*(n+1)  # 노드 개수만큼 지정
root = -1
x = 1  # 현재 열 위치 저장 변수
level_depth = 1  # 트리 최대 레벨 깊이

# 트리 초기화
for i in range(1, n+1):
    tree[i] = Node(i, -1, -1)

# 트리 만들기
for _ in range(n):
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    # 존재하는 경우 parent = number. 모든 노드에서 부모노드 찾을 수 있음.
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number

# root 찾기
for i in range(1, n+1):
    # 부모가 없는 노드가 root라고 가정
    if tree[i].parent == -1:
        root = i

# root 부터 중위순회 진행
in_order(tree[root], 1)

# 결과 초기화
result_level = 1
result_width = level_max[1] - level_min[1]+1

# 결과 구하기 (레벨, 최대 너비)
for i in range(2, level_depth+1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)
