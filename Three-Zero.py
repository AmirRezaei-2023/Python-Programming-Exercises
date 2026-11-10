
def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4

    return f(n-1) + f(n-2) + f(n-3)


n = int(input())
print(f(n))
