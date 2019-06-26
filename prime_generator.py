def sieve(ll,num):
    limitn = num+1
    not_prime_num = set()
    prime_nums = ''

    for i in range(2, limitn):
        if i in not_prime_num:
            continue

        for f in range(i*2, limitn, i):
            not_prime_num.add(f)
        if i>=ll:
            print(i,end=" ")

    return prime_nums

t = int(input())

for i in range(t):
	str =  input()
	l = str.split()
	ll = int(l[0])
	ul = int(l[1])
	print(sieve(ll,ul))