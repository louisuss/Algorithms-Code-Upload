class MyCircularQueue:
    def __init__(self, k):
        self.q = [None]*k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    # enqueue -> rear pointer 이동
    def enqueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2+1) % self.maxlen
            return True
        else:
            return False

    # dequeue -> front pointer 이동
    def dequeue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1+1) % self.maxlen
            return True

    def front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def rear(self):
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]

    def is_empty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def is_full(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None
