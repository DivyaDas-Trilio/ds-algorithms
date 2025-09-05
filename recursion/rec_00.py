def f1(str, i, n, osf):
    if(i==n):
        return
    
    f1(str, i+1, n, osf)
    osf = osf + str[i]
    print(osf, end="")
    
str = "abcde"
f1(str, 0, 5, "")