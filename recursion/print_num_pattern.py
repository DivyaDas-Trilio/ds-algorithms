def print_num_pattern(n):
    if(n==1):
        print(1)
        return
    for i in range(1, n+1):
        print(i, end='')
    print('')
    print_num_pattern(n-1)
    for i in range(1, n+1):
        print(i, end='')
    print('')
    
print_num_pattern(5)