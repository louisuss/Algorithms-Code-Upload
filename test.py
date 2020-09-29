a = [[2,1], [4,2], [2,3],[3,1]]

a = sorted(a, key=lambda x: (x[0], x[1]))
print(a)