def bin_to_dec(bin):
    bin = list(bin[::-1])
    num =0
    for index, item in enumerate(bin):
        if item == "1":
            num += pow(2, int(index))
            
    return num

# print(bin_to_dec("1"))
    
    
def print_bin(num, osf):
    if(bin_to_dec(osf) > num):
        return
    
    if(bin_to_dec(osf) == num):
        print(osf)
        
    print_bin(num, osf+"0")
    print_bin(num, osf+"1")
    
print_bin(10, "1")