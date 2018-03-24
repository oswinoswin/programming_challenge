#!/usr/bin/python3
import random
import sys

def toss_coin(attempts):
	random.seed()
	heads = 0
	tails = 0
	for i in range(attempts):
		if random.randint(1,2)%2 == 0:
			heads +=1
		else:
			tails+=1
	return (heads, tails)


if __name__ == "__main__":
	if len(sys.argv) == 2:
		attempts = int(sys.argv[1])
	else:
		attempts = 1000
	heads, tails = toss_coin(attempts)
	print("Result after {} attempts:\n heads: {}, tails: {}".format(attempts, heads, tails))
