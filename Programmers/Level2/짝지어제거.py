# deque 안에 인자는 iterable한 것만 들어감
from collections import deque
temp = deque()
print(temp)
s = 'baabaa'
s = deque(s)
print(s[1])
