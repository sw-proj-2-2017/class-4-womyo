def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
def fact(m):
    if m == 0:
        return 1
    else:
        return m * fact(m - 1)
while True:
    n = int(input("Enter n:"))
    if n < 0 :
        break
    else:
        m = int(input("Enter m:"))
        a = int(fact(n)/(fact(m)*fact(n - m)))
        print("C(%d,%d) = %d" %(n, m, a))






