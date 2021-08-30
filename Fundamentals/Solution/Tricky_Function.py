# Tricky Function
'''
Raju has got an interesting function F(n). The function can be defined as-
. F(0) = 0  
. F(1) = 1  
. F(n) = F(n/2), if n is even
. F(n) = F(n−1)+1, if n is odd

Given the value of n find F(n).

Input format
The first line of the input contains a single integer t denoting the number of test cases.
The first and the only line of each test case contains a single number n.

Output format
For each test case on a new line print the value of F(n).

Constraints
. 1 <= t <= 10^4
. 1 <= n <= 10^18

Example
Input
1
5

Output
2
'''
# SOLUTION - 30/8/2021 12:05PM
def tricky(n):
  if n == 0 or n == 1: return n
  elif n % 2 == 0: return tricky(n//2)
  else: return tricky(n-1)+1
  
for _ in range(int(input())):
  print(tricky(int(input())))
