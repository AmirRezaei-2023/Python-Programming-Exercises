a, b, c, d, e = map(int, input().split())
lst = [a, b, c, d, e]
j = 0
for i in range(4):
    if lst[j] < lst[i+1]:
        j = i + 1
    else:
        pass
print(j+1)