def exp(n,m):
	if m==0 and n==0:
		return 1
	if m==0:
		return 1
	if n==0:
		return 0
	else:
		return n*exp(n, m-1)

print(exp(0,0))