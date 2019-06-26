t = int(input())
ans = []

for ix in range(0,t):
    n = int(input())

    res = []

    for i in range(0,n):
        for j in range(i,n+1):
            if((i**2)+(j**2)==n):
                res.append("(")
                res.append(i)
                res.append(",")
                res.append(j)
                res.append(")")


    ans.append(res)
    print(end="")
print(end="")


for i in range(len(ans)):
    for j in range (len(ans[i])):
        print(ans[i][j],sep=" ",end="")
    print()