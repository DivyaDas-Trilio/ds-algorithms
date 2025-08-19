def reverse(s, i, n):
    if(i == n):
        return
    reverse(s, i+1,n)
    print(s[i], end='')
    
s = "Divya Jyoti Das"
n = len(s)
reverse(s, 0, n=n )