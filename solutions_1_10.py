#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:14:02 2020

@author: jagat
"""

from project_euler_1_10 import *


# problem 1
print('\n Problem 1:')
N = 1000
sum_of_multiples(3,5,N)

# problem 2
print('\n Problem 2:')
Max = 4*1000*1000
sum_of_fibonacci_terms(Max)


# problem 3
print('\n Problem 3:')
number = 600851475143
largest_prime_factor(number)


# problem 4
print('\n Problem 4:')
largest_palindrome = largest_palindrome_product(3)
print(" The largest palidrome from product of 2 three digits numbers is %d"%(largest_palindrome))