def tarsim (num, charcter):
    if charcter == "s":
        num = int(num)
        i = num
        while i>0:
            print(num*"*")
            i -= 1
    elif charcter == "t":
        num = int(num)
        while num>0:
            print(num*"*")
            num -= 1


x, y = input().split()
tarsim(x, y)