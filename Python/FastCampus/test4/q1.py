n = list(map(int, input()))
idx = len(n)//2

left = n[:idx]
right = n[idx:]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")