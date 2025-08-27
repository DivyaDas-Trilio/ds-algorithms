def calc_num_ways(n):
    if(n<=2):
        return n
    alone = calc_num_ways(n-1)
    pair = (n-1) * calc_num_ways(n-2)
    return alone + pair 

print(calc_num_ways(4))