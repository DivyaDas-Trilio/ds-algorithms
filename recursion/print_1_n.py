def print_1_n(num):
    if num == 0:
        return
    print_1_n(num-1)
    print(num)
    
if __name__ == '__main__':
    print_1_n(10)