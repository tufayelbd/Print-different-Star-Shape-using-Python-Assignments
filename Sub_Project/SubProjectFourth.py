def start(n):
    num=0
    for i in range(1,n+1):
        if(i%2>0):
            num=num+1
    j=num
    for i in range(1,num):
        print(" "*(num-1-i)+"* "*i+"  "*(num-i)+"* "*i)
        j=j-1
    print("* "*n)
    k=n
    for i in range(1,num):
        print("  "*(i)+"* "*(k-i-1))
        k=k-1


n=int(input())
if(n%2>0):
    start(n)
else:
    print("\tError: Sorry Enter An Odd Number : ")