
def winner(n):
    if n == 1:
        return 1

    return (winner(n - 1) + 1) % n + 1


n = int(input())
print(winner(n))
