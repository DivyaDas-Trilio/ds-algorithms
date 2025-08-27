def expo(a, b):
    if(b == 1):
        return a
    
    return a * expo(a, b-1)

print(expo(2,40))