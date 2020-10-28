x_list = []
y_list = []
x, y = 0, 0
for _ in range(3):
    x1, y1 = map(int, input().split())
    x_list.append(x1)
    y_list.append(y1)

for i in range(3):

    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]

print(x, y)