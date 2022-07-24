def main():
	int_list = []

	for a in range(2, 100+1):
		for b in range(2, 100+1):
			contains = False
			number = a**b
			for c in range(0, len(int_list)):
				if int_list[c] == number:
					contains = True
			if not contains:
				int_list.append(number)
	int_list.sort()
	print(len(int_list))


main()

# worked in python but not in go, since python
# lacks the integer overflow problem.
