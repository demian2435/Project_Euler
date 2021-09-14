def main():
	num = 600_851_475_143
	max_prime = 0

	while(num > 1):
		for i in range(2,num + 1):
			if num % i == 0:
				num = int(num / i)
				if (i > max_prime):
					max_prime = i
				break
	print(max_prime)
	

if __name__ == "__main__":
    main()