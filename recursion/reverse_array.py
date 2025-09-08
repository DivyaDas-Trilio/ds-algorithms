import array

def reverse_array(arr, i, n, rev_arr):
    if(i == n):
        return
    
    reverse_array(arr, i+1, n, rev_arr)
    rev_arr[i] = arr[i]
    
    return rev_arr

def optimized_reverse_array(arr, i, j):
    if(i==j):
        return
    
    arr[i], arr[j] = arr[j], arr[i]
    optimized_reverse_array(arr, i+1, j-1)
    return arr

# print(reverse_array([10,20,30,40,50], 0, 5, array.array("i", [])))
print(optimized_reverse_array([10,20,30,40,50], 0, 4))