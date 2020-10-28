
a, b = map(int, input().split())

res = str(a/b)
int_side, decimal_side = res.split('.')
if len(decimal_side) == 1:
    decimal_side += "0"
else:
    decimal_side = decimal_side[0:2]

res = int_side + '.' + decimal_side
print(res)