#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:59:20 2020

@author: jagat
"""
import math

def sum_of_multiples(a,b,N):
    '''
    Sum of multiples of numbers a,b below N
    '''
    N_a = math.floor(N/a)
    N_b = math.floor(N/b)
    N_ab = math.floor(N/(a*b))
    
    # Sum of Arithmetic progression
    S_a = a*(2 + (N_a-1))*N_a/2
    S_b = b*(2 + (N_b-1))*N_b/2
    S_ab = a*b*(2 + (N_ab-1))*N_ab/2
    
    # Since the last term is not included.
    if N%a == 0 or N%b == 0:
        S_n = S_a + S_b - S_ab - N
    else:
        S_n = S_a + S_b - S_ab
        
    print(" Sum of multiples of %d and %d below %d is %d"%(a,b,N,S_n))
    

def sum_of_fibonacci_terms(Max):
    import time
    Max = 4*1000*1000
    a = 1
    b = 2
    s = b
    c = 3
    start_time = time.time()
    while(c < Max):
        if (c%2 == 0):
           s = s + c
        a = b
        b = c
        c = a + b
    print(' Total_time = ' + str(time.time()-start_time))
    print(' Sum of even terms of fibonacci:%d'%s)


'''
Finds if the number is prime and returns the number
if the number is not prime, it returns the first factor where test of primes failed
'''                    
def is_number_prime(number):
        sqrt_num = int(math.floor(number**(.5)))
        #print(sqrt_num)
        if (number != 1 and number != 0):
            for j in range(2,sqrt_num+1):
                if (number%j==0):
                    #print(j)
                    return(j)
                if (j == sqrt_num):
                    return number

'''
Finds the largest prime factors recursively by computing all the factors of the number
It first finds a prime factor and then computes the quotient and then recursively applies 
the same procedure
'''            
def largest_prime_factor(number): 
    #input("Enter to continue:")
    if number!= 1:
        prime_factor = is_number_prime(number) 
        print(" The prime factor:%d"%(prime_factor))
        quotient = int(number/prime_factor)
        print(" The quotient:%d"%quotient)
        largest_prime_factor(quotient)
        
        
def largest_palindrome_product(num_digits):
    largest = 0
    for i in range(1,10**num_digits):
        for j in range(1,10**num_digits):
            test_number = 10**(2*num_digits) -10**(num_digits)*(i+j)+i*j
            if is_palindrome(test_number,2*num_digits):
                if test_number>largest:
                    largest = test_number
    return largest
            
def is_palindrome(number,total_digits):
    digits =[]
    test_number = number
    for i in range(0,total_digits):
        digits.append(test_number%(10))
        #print(digits)
        #reverse_number = reverse_number*10 + digit
        #input("Enter to continue")
        test_number = int(test_number/10)
        #print(test_number)
    if form_number(digits) == number:
        return True
    else:
        return False        
def form_number(digits):
    number = 0
    for i in digits:
        number = number*10 + i
    return number