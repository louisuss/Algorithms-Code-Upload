class Node:
    # 노드값, 다음 노드 가리키는 포인터
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        # 다음노드가 끝을 가리킴
        self.last = Node(item, self.last)

    def pop(self):
        # 마지막 아이템
        item = self.last.item
        # 이전값을 last에 저장
        self.last = self.last.next
        return item


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(3)
    stack.push(3)
    for _ in range(5):
        print(stack.pop())
