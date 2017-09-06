while True:
    f=1
    n = int(input('Enter a number:'))
    if n<0:
        break
    else:
        for i in range(1,n+1):
            f*=i
    print("%d!=%d" % (n,f))
