def printStar(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"* "*i)
    x=n-1
    for i in range(1,n):
        print(" "*i+"* "*x)
        x=x-1


n=int(input())
printStar(n)