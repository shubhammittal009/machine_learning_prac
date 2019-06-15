def genParanthesis(openB,closeB,n,s=[]):
	
	if(closeB==n):
		print(''.join(s))
		return

	else:
		if(openB>closeB):
			s.append(')')
			genParanthesis(openB,closeB+1,n,s)
			s.pop()
		if(openB<n):
			s.append('(')
			genParanthesis(openB+1,closeB,n,s)
			s.pop()
		return

genParanthesis(0,0,3)