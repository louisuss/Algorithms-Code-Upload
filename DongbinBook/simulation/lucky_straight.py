score = input()
left = list(score[:len(score)//2])
right = list(score[len(score)//2:])
if sum(list(map(int, left))) == sum(list(map(int, right))):
    print("LUCKY")
else:
    print("READY")