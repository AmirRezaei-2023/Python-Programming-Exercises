def tarsim (num1, num2, charcter):
    while num1>0:
        tol = num1
        arz = num1
        for i in range(tol):
            print(tol*charcter)
        num1 -= num2

x, y, c = input().split()
x = int(x)
y = int(y)
tarsim(x, y, c)