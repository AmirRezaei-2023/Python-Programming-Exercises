n, k = map(int, input().split())

i=0
stp = 1
while True:
    stp += k
    i += 1
    if stp%n == 1:
        break
    elif stp > n:
        stp -= n
        
print(i)