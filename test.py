from decimal import Decimal
import math
a = 26
b = 4
if a % b == 0:
    res = str(a/b) + "0"
else:
    res = str(round(a/b, 2))

print(res)
