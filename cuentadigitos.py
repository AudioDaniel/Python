def digits(n):
	c = 0
	for x in str(n):
		c = c+1
	return c


print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1