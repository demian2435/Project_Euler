def main():
	a = 0
	b = 0
	max_pal = 0

	for i in range(1000):
		for j in range(1000):
			prod = i *j
			str_prod = str(prod)
			if prod > 100000 and str_prod[0] == str_prod[-1] and str_prod[1] == str_prod[-2] and str_prod[2] == str_prod[-3]:
				if prod > max_pal:
					max_pal = prod
	print(max_pal)


if __name__ == "__main__":
    main()