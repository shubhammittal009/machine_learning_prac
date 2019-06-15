t = int(input())

for ix in range(0,t):
    n = int(input())

    for i in range(0,n):
        for j in range(i,n+1):
            if((i**2)+(j**2)==n):
                print("(",i,",",j,")",sep="",end=" ")
    print()
print()