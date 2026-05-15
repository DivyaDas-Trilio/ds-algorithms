## Unsorted Searching/ Linear Searching

def linear_search(arr, key):
    # for i in arr:
    #     if key == i:
    #         print("Found Key {0}".format(key))
    #         return True
    
    for index, val in enumerate(arr):
        if key == val:
            print("Found key {0} at position {1}".format(key, index))
            return True
    
    print("Not Found...")

arr = [2,1,8,7,5,0,3]
#key= 5
key = 90
linear_search(arr, key)