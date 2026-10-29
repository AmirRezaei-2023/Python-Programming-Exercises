num = int(input())
i = 1
jam_koli = 0
while i <= num:
    j = 1
    jam = 0
    while j<=i:
        print(j, end = "")
        jam += j
        j += 1
        if j<=i:
            print("+", end = "")
        else:
            pass
    print(" =", jam)
    i += 1
    jam_koli += jam
print(f"Total sum of series is: {jam_koli}")