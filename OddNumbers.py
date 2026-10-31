def is_prime (num1):
    num1 = int(num1)
    maghsom = num1 - 1
    while maghsom>1:
        if num1%maghsom == 0:
            break
        else:
            maghsom -= 1
    if maghsom == 1:
        print(num1)

def show_primes (start, finish):
    strt = int(start)
    fnsh = int(finish) + 1
    for i in range(strt, fnsh):
        is_prime (i)
        
x = input()
y = input()
show_primes(x, y)