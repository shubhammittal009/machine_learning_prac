n = int(input())

for i in range(1,n+2):
	print("* "*(i-2),"* "*(i-3),sep="")
	for ix in range(1,n+2-i):
		print(ix,sep=" ",end=" ")