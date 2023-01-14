students = int(input())
students_skills = list(map(int, input().strip().split()))[:students]

prog = [i for i, e in enumerate(students_skills) if e == 1]
math = [i for i, e in enumerate(students_skills) if e == 2]
pe = [i for i, e in enumerate(students_skills) if e == 3]
temp = [prog, math, pe]
teams = list(map(list, zip(*temp)))

print(len(teams))
for t in teams:
    for m in t:
        print(m+1, end=' ')
    print()
