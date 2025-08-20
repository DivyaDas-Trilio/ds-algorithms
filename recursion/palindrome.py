l_str, r_str = "", ""
def f(s, i, n):
    global l_str, r_str
    if(i==n):
        return
    l_str += s[i]
    f(s, i+1, n)
    r_str += s[i]
    if((l_str ==r_str)):
        print("Palindrome")
    
if __name__ == "__main__":
    s = "ABCDCB"
    n = len(s)
    f(s, 0, n)
   