# Sorcerer Sequence
'''
Sorcerer Sequence is a series of integer numbers in which the first term starts with a positive integer and the remaining terms are 
generated from the immediate previous term using the below recurrence relation :

. a(k+1) = a(k)^(1/2) for even a(k)
. a(k+1) = a(k)^(3/2) for odd a(k)

Given a number N your task is to print the space-separated Sorcerer Sequence using this number as the first term of the sequence.

Input Format
First-line contains an integer T, where T is the number of test cases.
For every Test case, there is only one integer input N.

Output Format
For each test case, in a new line print, the space-separated Sorcerer sequence for number N as the first term of the sequence.

Constraints
. 1 <= T <= 100
. 1 <= N <= 100

Example
Input1
2
8
5

Output
8 2 1
5 11 36 6 2 1

Explanation
In the first test case, we start with 8 and use the above formula to get the next terms, until we reach 1.
In the second test case, we start with 5, next digit is (sqrt(5)*sqrt(5)*sqrt(5)) = 11, and so on.
'''
# SOLUTION - 19/8/2021 6:00PM
for _ in range(int(input())):
  array = [int(input())]
  while array[-1] != 1:
    if array[-1] % 2 == 0: array.append(int(array[-1]**0.5))
    else: array.append(int(array[-1]**1.5))
  print(*array)
