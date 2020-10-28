n = int(input())
cnt = 0
number = 1
idx = 0

while n > 0:
    if n < number:
        number = 1
    n -= number
    number += 1
    cnt += 1
print(cnt)