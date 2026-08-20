def sum(num):
	if num == 0:
		return 0
	else:
		return sum(num-1)+num


if __name__ == '__main__':
	num = 10
	print(sum(num))
	


