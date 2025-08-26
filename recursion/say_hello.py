def say_hello(n):
    if(n==0):return
    
    say_hello(n-1)
    print('hello ', n)
    
    
if __name__ == '__main__':
    say_hello(10)