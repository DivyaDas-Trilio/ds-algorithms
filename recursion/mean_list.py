def mean_list(lst, i, n):
    # base case
    if i == n:
        return lst[i]
    # Recursive case
    sum = lst[i] + mean_list(lst, i+1,n)
    # self work
    return sum
    
if __name__ == '__main__':
    lst = [1,2,3,4,5]
    print(mean_list(lst, 0, 4)/len(lst))