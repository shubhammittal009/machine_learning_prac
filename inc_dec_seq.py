num = int(input())

val = 0
l = []
for i in range(1,num+1):
	n = int(input())
	l.append(n)
flag = 0
val = 0
for i in range(0,num-1):
	if(l[i]<l[i+1]):
		break
	i=1+1
	val = i
for i in range(val,num-1):
	i=i+1
	if(i+1<num and l[i]>l[i+1]):
		print(false)
		break
if(flag!=0):
	print("true")