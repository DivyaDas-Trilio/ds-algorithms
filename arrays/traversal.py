arr = [1,2,3,4,5,6,7,8,9]
def main(i, n, arr):
    
    # for i in arr:
    #     print(i)
    
    # for _ in range(10):
    #     print(_)
    
    # for index, val in enumerate(arr):
    #     print(index, val)
    if (i==len(arr)):
        return
    
    main(i+1, n, arr[i])
    print(arr[i]) 
    

i=0
n = len(arr)  
main(i, n, arr)
