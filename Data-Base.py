def linearSearch(arr , size , key):
	for i in range (size):
		if arr[i] == key:
			return 1
	return 0

n, q = input().split()
n = int(n)
q = int(q)
ns = input().split()
for i in range(n):
    ns[i] = int(ns[i])
qs = []
for i in range(q):
    srch = input()
    qs.append(srch)

#print(qs)
qss = []
for i in qs:
    num = int(i.split()[1])
    qss.append(num)
#print(qss)
for i in qss:
    print(linearSearch(ns, n, i))