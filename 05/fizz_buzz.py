#!/usr/bin/python

def fizz_buzz(n):
	if n % 15 == 0:
		return "FizzBuzz"
	if n % 3 == 0:
		return "Fizz"
	if n % 5 == 0:
		return "Buzz"
	return str(n)

for n in range(100):
	print(fizz_buzz(n))


