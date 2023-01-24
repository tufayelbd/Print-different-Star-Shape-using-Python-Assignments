def printStar(n):
    x=0
    for i in range(1,n+1):
        if(i%2>0):
            x=x+1
    #print(x)
    num=x
    for j in range(1,x+1):
        print(" "*(num+1)+"* "*j)
        num=num-1
       # m=m-1
    print("* "*n)
    for i in range(1,x):
        print("* "*(x-1)+"  "+"* "*(x-1))


n=int(input())
if(n%2>0):
    printStar(n)
else:
    
    
    print("Error: Enter An Odd Number")