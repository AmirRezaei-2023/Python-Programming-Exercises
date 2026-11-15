init_list = input().split()
n = len(init_list)
ref_dict = {}
for i in range(n):
    init_list[i] = int(init_list[i])
#print(init_list)
yekta = []
yekta.append(init_list[0])
for i in init_list:
    if i in yekta:
        pass
    else:
        yekta.append(i)
#print(yekta)
for i in yekta:
    ref_dict[i] = 0
#print(ref_dict)
for i in init_list:
    for j in ref_dict.keys():
        if i == j:
            ref_dict[j] += 1
#print(ref_dict)
max_val = max(ref_dict.values())
max_inx = []
for i in ref_dict.keys():
    if ref_dict[i] == max_val:
        max_inx.append(i)

for i in range(len(max_inx)):
    max_inx[i] = int(max_inx[i])
print(min(max_inx), max_val)