def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
def combination(n, m):
        return fact(n)/(fact(m)*fact(n - m))

def recursive(n, m):
    if n == m or m == 0:
        return 1
    else:
        return recursive(n - 1,m - 1) + recursive(n - 1, m)
while True:
    n = int(input("Enter n:"))
    if n < 0 :
        break
    else:
        m = int(input("Enter m:"))
        print("C(%d,%d) = %d" %(n, m, combination(n, m)))
        print("C(%d,%d) = %d" %(n, m, recursive(n, m)))








