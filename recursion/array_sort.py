def array_sort(arr,i,n):
    if i == n-1:
        return True
    
    if(arr[i] >  arr[i+1]):
        return False
    return array_sort(arr, i+1,n)
    
    
print(array_sort([1,2,3],0,3))


# [1]
# [1,2]
# [1,2,3]