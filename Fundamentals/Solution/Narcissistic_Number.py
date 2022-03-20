# Narcissistic Number
'''
Prepbuddy wants you to know the Narcissistic number, so she asked you to write a program to check 
whether a number is a Narcissistic number or not.
Hint: An n-digit number that is the sum of the nth powers of its digits is called a n-narcissistic number.

Input format
The first line contains an integer, the number of test cases T. 
T test cases follow. Each test case contains a positive integer N.

Output format
For each test case, in a new line, print "Yes" if it is a Narcissistic number else print "No".

Constraints
. 1 <= T <= 10
. 1 <= N < 10^4

Time Limit
1 second

Example
Input
2
371
8207

Output
Yes
No

Example:
In the first test case,N = 371, it is a 3 digit number.
3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371.
'''
# SOLUTION - 20/3/2022 11:46PM
for _ in range(int(input())):
  number = int(input())
  n_sum = 0; n_digit = 0
  temp1 = temp2 = number
  while temp1 != 0:
    n_digit += 1
    temp1 //= 10
  while temp2 > 0:
    digit = temp2 % 10
    n_sum += digit ** n_digit
    temp2 //= 10
  if number == n_sum:
    print('Yes') 
  else:
    print('No')
