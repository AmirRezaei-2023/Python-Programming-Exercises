
s = input()
p = input()

for i in range(len(s) - len(p) + 1):
    if s[i:i+len(p)] == p:
        print(i + 1, end=" ")
