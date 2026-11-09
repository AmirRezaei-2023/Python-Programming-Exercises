student_dict = {}
while True:
    round = input().split()
    if round[0] == "End":
        break
    else:
        student_dict[round[0]] = float(round[-1])
#print(student_dict)
mean = sum(student_dict.values()) / len(student_dict)
winners = []
for key in student_dict.keys():
    if student_dict[key] >= mean:
        winners.append(key)
    else:
        pass
print(winners)
add = [] 
for i in winners:
    add.append(student_dict[i])
mean_2 = sum(add) / len(add)
print(mean_2)