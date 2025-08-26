def sum_digits(n):
    
    if(n==0):
        return 0
    quo = n//10
    rem = n%10
    
    return rem + sum_digits(quo)
    
print(sum_digits(123456789))