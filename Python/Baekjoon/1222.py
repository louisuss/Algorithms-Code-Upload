def solve(school):
    a = [0]*2000001
    if len(school) == 1:
        return -1
    elif len(school) == 2:
        if 1 in school:
            return 2
    else:
        max_val = len(school)
        cnt = 0


n = int(input())
school = list(map(int, input().split()))




