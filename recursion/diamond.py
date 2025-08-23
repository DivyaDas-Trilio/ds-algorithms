def print_diamond(r, c):
    if(r == 0):
        return
    if(r > c):
        print('*', end='')
        print_diamond(r, c+1)
    else:
        print('')
        print_diamond(r-1, 0)
        
def reverse_print_problem(r, c):
    if(r==0):
        return
    if(r <= c):
        print('*', end='')
        reverse_print_problem(r, c-1)
    else:
        print('')
        reverse_print_problem(r-1, 5)
    
        
#print_diamond(5, 0)

reverse_print_problem(5, 5)