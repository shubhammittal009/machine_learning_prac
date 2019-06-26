t = int(input())
ans = []

for ix in range(0,t):
    n = int(input())

    res = []

    for i in range(0,n):
        for j in range(i,n+1):
            if((i**2)+(j**2)==n):
                res.append((i,j))

    # for i in (len(res)):
    # 	print(res[i])
    ans.append(res)
    print(res)
print()