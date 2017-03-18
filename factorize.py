#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  factorize.py
#  
#  Copyright 2017 Jesse Rominske
#  
#  Program to print the prime power factorization of its argument

import math # we want math
import sys

# returns primality of i
def isPrime(i, primes):
	if i == 2: return True
	for p in primes:
		if p <= math.sqrt(i):
			if i % p == 0: return False
		else: return True

# produces a list of the factors of n
def generateFactors(n):
	primes = [] # list of primes we will use to compare primality
	factors = [] # list of factors we have found so far
	bound = int(math.ceil(math.sqrt(n) + 1)) # bound to limit looping
	#separate loop for 2 so we can skip all even numbers in the main loop
	while n % 2 == 0:
		factors.append(2)
		n /= 2
	i = 3 # the odd number we will be checking for primality and division
	while i < bound:
		if isPrime(i, primes):
			primes.append(i)
			divides = False
			while n % i == 0:
				divides = True
				factors.append(i)
				n /= i
			if divides: bound = int(math.ceil(math.sqrt(n) + 1))
		i += 2 # increase i by two to skip all even numbers
	if n > 1: factors.append(n) # this must be larger than all p, so the list is still sorted
	return factors

# creates prime power factorization from the list of factors of n
def condense(factors):
	primePower = [0, 0]
	powerList = []
	for f in factors:
		if f == primePower[0]: # if we are still looking at the same factor
			primePower[1] += 1 # increment power of factor
		else:
			powerList.append(primePower) # stick previous one on there
			primePower = [f, 1] # record instance of new factor
			
	powerList.append(primePower) # stick the last one on there
	return powerList[1:] # we stuck [0, 0] on there, so get rid of that

# make the list nice to print
def beautify(powerList):
	s = ""
	for pair in powerList:
		s += "(" + str(pair[0]) + "^" + str(pair[1]) + ")"
	return s	

# main program structure
def main(args):
	while True:
		arg = raw_input("Enter integer: ")
		
		# takes int if given, converts from ASCII if not
		try:
			n = int(arg)
		except (TypeError, ValueError):
			i = 0
			n = 0
			for c in arg:
				n += ord(c) * pow(128, i) # converts from base-128
				i += 1
		
		# case handling for various values of n		
		if n == 0:
			print("0 has no factorization")
		elif n == 1:
			print("1 has no unique factorization")
		elif n == -1:
			print(str(n) + " = (-1^(2k+1))")
		elif n < 0:
			powersList = "(-1^(2k+1))" + beautify(condense(generateFactors(-n)))
			print(str(n) + " = " + powersList)
		else: 
			powersList = beautify(condense(generateFactors(n)))
			print(str(n) + " = " + powersList) # print the answer

if __name__ == '__main__':
    sys.exit(main(sys.argv))
