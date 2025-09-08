def reverse_array(arr, i, n, rev_arr):
    if(i == n):
        return
    
    reverse_array(arr, i+1, n, rev_arr)
    rev_arr.append(arr[i])
    
    return rev_arr

print(reverse_array([10,20,30,40,50], 0, 5, []))