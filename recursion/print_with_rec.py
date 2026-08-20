# def p_n(n):
#     if n ==0:
#         return n
#     else:
#         print(n)
#         p_n(n-1)-1
#         return n
#
# def n_p(n):
#     if n==0:
#         return
#     else:
#         print(n)
#         n_p(n-1)



def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        n1 = fib(n-1)
        print(n1)
        n2 = fib(n-2)
        print(n2)
        return n1+n2
print(fib(7))