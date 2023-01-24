def printStar(n):
    print("* "*n)
    for i in range(1,n):
        print("  "*i+"* "*n)


n=int(input())
printStar(n)