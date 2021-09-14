def main():
	a = 0
	b = 1
	c = 2
	sum = 0
	while(c < 4_000_000):
		if c % 2 == 0:
			sum += c
		a = b
		b = c
		c = a + b
	print(sum)

if __name__ == "__main__":
    main()