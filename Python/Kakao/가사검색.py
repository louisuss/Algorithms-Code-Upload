import re


class Node:
    def __init__(self, word=""):
        self.word = word
        self.child = {}
        self.length = 0


class Trie:
    def __init__(self):
        self.root = Node()
        self.key_list = {}

    def create(self, words, reverse=False):
        for word in words:
            if reverse:
                word = word[::-1]

            # 중복 키 체크
            if word not in self.key_list:
                # 키 중복 없으면 키, 길이 추가
                self.key_list[word] = len(word)
                # 루트부터 시작
                current_node = self.root
                for w in word:
                    # 루트 노드 자식에 연결안된 경우 연결
                    if w not in current_node.child:
                        current_node.child[w] = Node(w)
                    # 노드 변경
                    current_node = current_node.child[w]
                # 마지막 노드에서 길이 정보 추가
                current_node.length = len(word)

    def search(self, word):
        cnt = 0
        current_node = self.root
        for w in word:
            if w not in current_node.child:
                if w == "?":
                    stack = []
                    len_w = len(word)
                    len_q = word.count("?")

                    # 모두 ?
                    if len_q == len_w:
                        for i in self.key_list.values():
                            # 길이가 같으면 다 같음
                            if i == len_w:
                                cnt += 1
                        break

                    # 현재 노드 자식 노드를 스택에 삽입
                    for node in current_node.child.values():
                        # (노드, 길이)
                        stack.append((node, 1))

                    # dfs
                    while stack:
                        current_node, current_depth = stack.pop()
                        # 현재 노드의 끝을 나타내는 노드, 깊이가 ?의 개수와 같으면 매칭
                        if current_node.length == len(word) and current_depth == len_q:
                            cnt += 1

                        # 현재 깊이가 ? 개수보다 작은 경우
                        if current_depth < len_q:
                            # 반복
                            for node in current_node.child.values():
                                stack.append((node, current_depth+1))
                    break
                else:
                    break
            current_node = current_node.child[w]
        return cnt


def solution(words, queries):
    answer = []
    dic = {}
    trie = Trie()
    trie.create(words, False)

    reversed_trie = Trie()
    reversed_trie.create(words, True)

    for query in queries:
        if query not in dic:
            if query.startswith('?'):
                # 접미사 ? 의 경우 뒤집기
                answer.append(reversed_trie.search(query[::-1]))
            else:
                answer.append(trie.search(query))
            dic[query] = answer[-1]
        else:
            answer.append[dic[query]]
    return answer


class Node:
    def __init__(self, data=None):
        self.data = data
        self.cnt = 0
        self.child = []

    def add(self, data):
        for node in self.child:
            if node.data == data:
                node.cnt += 1
                return node
        else:
            new_node = Node(data)
            self.child.append(new_node)
            new_node.cnt += 1
            return new_node


class Trie:
    def __init__(self):
        self.head = Node()
        self.current = self.head

    def append(self, word):
        N = len(word)
        self.current = self.head.add(N)
        for ch in word:
            self.current = self.current.add(ch)

    def find(self, query):
        # 문자열 길이 비교
        N = len(query)
        self.current = self.head
        # 쿼리 길이와 문자 길이 같은 노드인지 확인후 현재노드로 선택
        for node in self.current.child:
            if node.data == N:
                self.current = node
                break
        else:
            return 0

        # query와 비교
        for ch in query:
            if ch == '?':
                # ?만나면 현재까지 일치한 word 수 리턴
                return self.current.cnt
            else:
                # 자식 노드에서 같은 문자 찾고 현재 노드 이동
                for node in self.current.child:
                    if node.data == ch:
                        self.current = node
                        break
                else:
                    return 0


def solution2(words, queries):
    tri_fw = Trie()
    tri_bw = Trie()
    for word in words:
        tri_fw.append(word)
        tri_bw.append(word[::-1])
    answer = []
    for query in queries:
        # 접두사 ?
        if query[0] == '?':
            # backward
            # 쿼리 뒤집기
            answer.append(tri_bw.find(query[::-1]))
        else:
            # forward
            answer.append(tri_fw.find(query))
    return answer


# 효율성 문제
def solution3(words, queries):
    answer = []
    words = set(words)  # 가사 중복 제거
    checked_query = {}

    for query in queries:
        cnt = 0
        q_len = len(query)

        # 같은 쿼리 반복 수행 제거
        if checked_query:
            if query in [checked_query.keys()]:
                answer.append(checked_query[query])
                break

        for word in words:
            if q_len == len(word):
                for a, b in zip(query, word):
                    check = True
                    if a == b or a == '?':
                        continue
                    else:
                        check = False
                        break
                if check:
                    cnt += 1
        answer.append(cnt)
        checked_query[query] = cnt

    return answer

# 효율성 문제


def solution4(words, queries):
    answer = []
    words = set(word)

    for query in queries:
        query = query.replace('?', '.')
        checked_query = {}
        cnt = 0
        len_q = len(query)

        if checked_query:
            if query in checked_query:
                answer.append(checked_query[query])
                break

        for word in words:
            if re.findall(query, word) and len_q == len(word):
                cnt += 1
        answer.append(cnt)
    return answer
