# 딕셔너리 리스트 연결

N, M = map(int, input().split())
team_mem, mem_team = {}, {}

for i in range(N):
    team_name, mem_num = input(), int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name, q = input(), int(input())
    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)

# N, M = map(int, input().split())
# girl_gp = {}

# for _ in range(N):
#     gp_name = input()
#     name = []
#     for _ in range(int(input())):
#         name.append(input())
#     girl_gp[gp_name] = sorted(name)

# name = []
# q = []
# for _ in range(M):
#     name.append(input())
#     q.append(int(input()))


# def solution(name, q):
#     if q == 0:
#         for n in girl_gp[name]:
#             print(n)
#     else:
#         for gp in girl_gp:
#             if name in girl_gp[gp]:
#                 print(gp)

# for a, b in zip(name, q):
#     solution(a, b)
