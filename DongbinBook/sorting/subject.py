# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sungyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90
n = int(input())
students = []
for _ in range(n):
    student = input().split()
    name = student[0]
    kor, eng, math = map(int, student[1:])
    students.append([name, kor, eng, math])

result = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for res in result:
    print(res[0])
