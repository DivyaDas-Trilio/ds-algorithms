def subsequence(arr, i, n, osf):
    if(i == n):
        if sum(osf) == 3:
            print(osf)
        return
    osf.append(arr[i])
    subsequence(arr, i+1, n, osf)
    osf.remove(arr[i])
    subsequence(arr, i+1, n, osf)


if __name__ == '__main__':
    arr = [1,2,3]
    osf = []
    subsequence(arr, 0, 3, osf)