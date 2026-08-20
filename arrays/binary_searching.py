class Test:
    def binary_search(self, arr, key):
        start = 0
        end = 9
        mid = (start + end)//2
        if(arr[start]==key or arr[end] == key or arr[mid]==key):
            return -1
        if(key > arr[end] or key < arr[start]):
            return -1
        
        while(arr[mid] != key):
            if (arr[start] > arr[end]):
                return -1
            if(arr[mid] < key):
                start = mid
                mid = (start + end)//2
            if(arr[mid] > key):
                end = mid
                mid = (start + end)//2
                
        return mid
            
                
    
t = Test()
arr = [10,20,30,40,50,60,70,80,90,100]
key = 100
print(t.binary_search(arr, key))