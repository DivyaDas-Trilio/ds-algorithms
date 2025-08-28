# def move_zeroes(num):
#     count = 0
    
#     for idx, val in enumerate(num):
#         if val ==0:
#             count += 1
#             num.remove(val)
            
#     for i in range(count):
#         num.append(0)
    
#     return num

def move_zeroes(num):
    temp= 0
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if(i == j):
                break
            if(num[i] == 0 and num[j] != 0):
                # temp = num[i]
                # num[i] = num[j]
                # num[j] = temp
                num[i], num[j] = num[j], num[i] # pythonic way
            continue
    return num
        
print(move_zeroes([0,12, 0,1,0,0,3,12]))
            