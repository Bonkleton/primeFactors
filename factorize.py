#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  factorize.py
#  
#  Copyright 2017 Jesse Rominske <bonkie@ALTRON-UbuntuStudio>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Program to print the prime power factorization of its argument:
#    python factorize.py <number>

import math
import sys

# returns primality of i
def isPrime(i, primes):
	for p in primes:
		if p <= math.sqrt(i):
			if i % p == 0: return False
		else: return True

# produces a list of all primes up to the size of the square root of n
def generatePrimes(n):
	primes = [2]
	bound = int(math.ceil(math.sqrt(n) + 1))
	for i in range(3, bound):
		if isPrime(i, primes):
			primes.append(i)
	return primes

# produces a list of the factors of n
def checkFactors(n, primes):
	factors = []
	for p in primes:
		while n % p == 0:
			factors.append(p)
			n = n / p
	if n > 1: factors.append(n) # this must be larger than all p, so the list is still sorted
	return factors

# creates prime power factorization from the list of factors of n
def condense(factors):
	primePower = [0, 0]
	powerList = []
	for f in factors:
		if f == primePower[0]: # if we are still looking at the same factor
			primePower[1] = primePower[1] + 1 # increment power of factor
		else:
			powerList.append(primePower) # stick previous one on there
			primePower = [f, 1] # record instance of new factor
			
	powerList.append(primePower) # stick the last one on there
	return powerList[1:] # we stuck [0, 0] on there, so get rid of that
	
# makes the prime power factorization much nicer to look at
def powerString(powerList):
	s = ""
	for pair in powerList:
		s = s + "(" + str(pair[0]) + "^" + str(pair[1]) + ")"
	return s

# main program structure
def main(args):
	n = int(args[1])
	
	primes = generatePrimes(n)
	factors = checkFactors(n, primes)
	powersList = powerString(condense(factors))
	
	print(str(n) + " = " + powersList)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
