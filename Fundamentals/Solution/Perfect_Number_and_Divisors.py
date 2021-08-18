# Perfect Number and Divisors
'''
Have you heard of Perfect numbers? If not let me tell you what is it, Perfect Numbers are integers that are equal to the 
sum of all its divisors except that number itself. Now, given an integer N,  write a program to print true if it is a perfect 
number or false if it is not a perfect number.

Input format
The first line contains the number of test cases T. 
Each test case contains an integer N is provided.

Output format
For each test case on a new line, print true or false depending on N.

Constraints
. 1 <= T <= 10
. 1 <= N <= 100

Example
Input
2
28
96

Output
true
false
'''
# SOLUTION - 18/8/2021 1:32PM	
for _ in range(int(input())):
  number = int(input())
  print('true') if sum([num for num in range(1, number) if number % num == 0]) == number else print('false')
