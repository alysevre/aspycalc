def add(x,y):
	""" (num, num) -> num

	Returns the sum of x and y.

	>>>add(2,3)
	5
	>>>add(0.75,0.9)
	1.65
	"""

	result = x + y
	return result


def subtract(x,y):
	""" (num, num) -> num

	Returns the result of subtracting y from x.

	>>>subtract(2,3)
	-1
	>>>subtract(0.75,0.05)
	0.7
	"""

	result = x - y
	return result


def multiply(x,y):
	""" (num, num) -> num

	Returns the product of x and y.

	>>>multiply(2,3)
	6
	>>>multiply(0.75, 2)
	1.5
	"""

	result = x * y
	return result


def divide(x,y):
	""" (num, num) -> float

	Returns the quotient of x over y.

	>>>divide(2,3)
	0.6666666666666666
	>>>divide(10,2)
	5.0
	"""

	result = x / y
	return result


def power(x,y):
	""" (num, num) -> num
	
	Returns a number equalling x to the power of y.

	>>>power(2,3)
	8
	>>>power(0.75,2)
	0.5625
	"""

	result = x ** y
	return result


def sqrt(x):
	""" (num) -> float

	Returns the square root of x.

	>>>sqrt(4)
	2.0
	>>>sqrt(2)
	1.4142135623730951
	"""

	result = x ** 0.5
	return result

