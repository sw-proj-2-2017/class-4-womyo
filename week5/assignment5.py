import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    if n <= 1:
        return n
    else:
        answer = [0, 1]
        for i in range(2, n + 1):
            answer.append(answer[i - 1] + answer[i - 2])
        return answer[n]

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))