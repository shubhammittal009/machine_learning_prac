n = int(input())
str =  input()
l = str.split()
l = list(map(int, l))
l.sort()

for i in range(len(l)):
    print(l[i],end=" ")