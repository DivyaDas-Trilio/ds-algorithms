def f1(str, i, n, osf):
    if(i>=n):
        print(osf)
        return
    if(i%2 == 0):
        osf = osf + str[i]
    f1(str, i+2, n, osf)
    
str = "abcdefg"
f1(str, 0, 7, "")