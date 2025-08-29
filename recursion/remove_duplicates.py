def remove_duplicates(nums):
    d={}
    list_nums = []
    for i in range(len(nums)):
        key = nums[i]
        if key in d.keys():
            d[key] = d[key] + 1
        else:
            d[key] = 1
    k = len(d.keys())
    nums = list(d.keys())
    
    #nums = list_nums.extend(['_' * (len(nums) - len(list_nums))])
    
    return nums

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))