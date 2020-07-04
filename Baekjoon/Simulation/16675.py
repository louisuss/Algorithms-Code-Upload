# 문자를 숫자로 매핑
ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())

if ML == MR and (ML+2) % 3 in [TL, TR]:
    print('TK')
elif TL == TR and (TL+2) % 3 in [ML, MR]:
    print('MS')
else:
    print('?')

# ML, MR, TL, TR = input().split()
# # S R P
# PRS = {
#     'P':0,
#     'R':1,
#     'S':2
# }

# if PRS[ML] == PRS[MR] and ((PRS[ML]+2) % 3 == PRS[TL] or (PRS[ML]+2) % 3 == PRS[TR]):
#     print('TK')
# elif PRS[TL] == PRS[TR] and ((PRS[TL]+2) % 3 == PRS[ML] or (PRS[TL]+2) % 3 == PRS[MR]):
#     print('MS')
# else:
#     print('?')
