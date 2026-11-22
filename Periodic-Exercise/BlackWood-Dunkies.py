n = int(input())
lst = []
i, j = 0, 0
while True:
    if (j>5000) or (i>5000):
        break
    else:
        lst.append([i,j])
        i += 1
        j += 1
    if (j>5000) or (i>5000):
        break
    else:
        lst.append([i,j])
        i += 1
        j -= 1
    if (j>5000) or (i>5000):
        break
    else:
        lst.append([i,j])
        i += 1
        j += 1
    if (j>5000) or (i>5000):
        break
    else:
        lst.append([i,j])
        i -= 1
        j += 1

for i in range(n):
    indx = -1
    inp = input().split()
    for j in range(len(lst)):
        if (lst[j][0] == int(inp[0])) and (lst[j][1] == int(inp[1])):
            indx = j
        else:
            pass
    print(indx)