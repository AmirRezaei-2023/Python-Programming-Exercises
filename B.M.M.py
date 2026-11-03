def findmin (x1, x2, x3, x4, x5):
    if x1>=x2:
        minm = x2
    else:
        minm = x1
    if minm>=x3:
        minm = x3
    else:
        minm = minm
    if minm>=x4:
        minm = x4
    else:
        minm = minm
    if minm>=x5:
        minm = x5
    else:
        minm = minm
    while minm>0:
        if (x1%minm == 0) and x2%minm == 0 and x3%minm == 0 and x4%minm == 0 and x5%minm == 0:
            return minm
        else:
            minm -= 1

    
    



numb1, numb2, numb3, numb4, numb5 = map(int, input().split())
print(findmin(numb1, numb2, numb3, numb4, numb5))