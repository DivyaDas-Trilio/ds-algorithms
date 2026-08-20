def fib(n):
	if n == 0 or n == 1:
		return n

	subprob1 = fib(n-1)
	subprob2 = fib(n-2)

	return subprob1 + subprob2

print(fib(6)) 