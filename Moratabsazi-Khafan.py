number_of_students = int(input())
ref_dict = {}
for j in range(number_of_students):
    name = input()
    ref_dict[j] = []
    val = []
    courses = input().split()
    for i in range(len(courses)):
        courses[i] = float(courses[i])
    grades = courses[1:]
    mean = sum(grades)//courses[0]
    val.append(mean)
    sports = input().split()
    val.append(int(sports[0]))
    val.append(name)
    ref_dict[j] = val
#print(ref_dict)
vals = []
for i in ref_dict.keys():
    vals.append(ref_dict[i])
#print(vals)
n = len(vals)
for i in range(n):
    j = i
    while j>0 and ((vals[j][0] > vals[j-1][0]) or
                ((vals[j][0] == vals[j-1][0]) and (vals[j][1] > vals[j-1][1]))):
        vals[j], vals[j-1] = vals[j-1], vals[j]
        j -= 1
#print(vals)
for i in range(n):
    print(vals[i][-1])