data = []
while True:
    x, y, z = map(int, input().split())
    if x == 0 or y == 0 or z == 0:
        break
    lis = [x,y,z]
    lis.sort()
    data.append(lis)

for i in range(len(data)):
    x = data[i][0]
    y = data[i][1]
    z = data[i][2]
    if (x*x + y*y) == z*z:
        print('right')
    else:
        print('wrong')
