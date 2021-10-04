# Print GCD
'''
Let's begin with a very simple question. 
You are given two integers represented by N and M, your task is to print GCD(Greatest Common Divisor) of N and M.

Input format
The first line contains an integer T denoting the number of test cases.
For the next T lines, each line contains two integers represented by N and M.

Output format
For each test case on a new line, print GCD of N and M.

Constaints
. 1 <= T <= 10
. 1 <= N <= 10^5
. 1 <= M <= 10^5

Example
Input
2
4 10
6 9

Output
2
3
'''
# SOLUTION - 4/10/2021 10:16AM	
for _ in range(int(input())):
  n, m = map(int, input().split())
  for i in range(min(n, m), 0, -1):
    if n % i == 0 and m % i == 0:
      gcd = i
      break
  print(gcd)
