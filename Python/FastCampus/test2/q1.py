n, k = map(int, input().split())
course = []
s = 0
lst = list(map(int, input().split()))
for l in lst:
    s += l
    course.append(s)

direction = True
start = 0
end = course[-1]
position = 0

if (k // end) % 2 == 1:
    direction = False
else:
    direction = True

position = k % end

# 되돌아오는 경우
if not direction:
    position = end - position

for i in range(len(course)):
    if position < course[i]:
        print(i+1)
        break
