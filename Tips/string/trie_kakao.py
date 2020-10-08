class Node:
    def __init__(self, char, data=None):
        # 노드 글자
        self.char = char
        # 마지막 노드일 경우 단어
        self.data = data
        # 해당 노드를 거쳐갈 경우, 가능한 글자 개수
        self.possible_word = 0
        # trie 자식 노드들
        self.children = {}


class Trie:
    def __init__(self):
        # 시작 노드
        self.head = Node(None)

    def insert(self, strs):
        current_node = self.head
        for char in strs:
            if char not in current_node.children:
                # 다음 문자 등록
                current_node.children[char] = Node(char)

            # 다음 노드로 이동
            current_node = current_node.children[char]
            # 가능한 글자 개수 증가
            current_node.possible_word += 1

        # 마지막 글자 -> 해당 trie 최종 문자를 저장
        current_node.data = strs

    def search(self, strs):
        current_node = self.head
        for char in strs:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        # 해당 노드까지 왔을 때 만들 수 있는 문자 개수가 1인 경우
        if current_node.possible_word == 1:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        result = []
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
                subtrie = current_node
            else:
                return []

        # 노드들
        stack = list(subtrie.children.values())

        # dfs. 단어 완성
        while stack:
            node = stack.pop()
            if node.data != None:
                result.append(node.data)
            stack.extend(list(node.children.values()))
        return result


def solution(words):
    cnt = 0
    word_trie = Trie()
    for word in words:
        word_trie.insert(word)

    for word in words:
        # 단어 끝까지 돌았지만 possible_word가 1이 아닌 경우 확인
        already_find = False

        for i in range(1, len(word)+1):
            # 트라이에서 해당단어의 인덱스를 늘려가며 검색하여 최소 필요 단어 탐색
            if word_trie.search(word[:i]):
                # 최소 철자검색 수
                cnt += len(word[:i])
                already_find = True
                break
        # 철자 다 입력하는 경우
        if not already_find:
            cnt += len(word)
    return cnt


print(solution(["banana", "go", "gone", "bandana"]))
