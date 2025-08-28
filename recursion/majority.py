from typing import List

def majorityElement(nums: List[int]):
    max_digit = 0
    maj = 0
    for i in range(len(nums)):
        val = nums[i]
        max_count = 0
        for j in range(len(nums)):
            if(nums[j] == val):
                max_count += 1
                
        if maj < max_count:
            maj = max_count
            max_digit= val
            
    return max_digit

def optimized_majorityElement(nums: List[int]):
    d={}
    for i in range(len(nums)):
        if nums[i] in d.keys():
            key = nums[i]
            d[key] += 1
        else:
            d[nums[i]] = 1
         
    return max(d, key=d.get)
    

print(optimized_majorityElement([1,2,2,2,1,2,2]))
#print(majorityElement([1, 1, 1, ,2, 2, 2]))