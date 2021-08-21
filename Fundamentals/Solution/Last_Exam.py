# Last Exam
'''
Rahul always wanted to be a Computer Science professor in a reputed college. Right now he is just one step away from achieving his goal. 
He just needs to write a program that will print the last digit of (1018)^N for various values of N. Your task is to help Rahul achieve his goal.

Input format
First line contains test case T.
T test cases follow,The one and only line contains an integer N.

Output format
For each test case, print last digit of (1018)^N

Constraints
. 1 <= T <= 100
. 0 <= N <= 10^8

Example
Input
2
2
3

Output
4
2

Sample test case explanation
T = 2
N = 2
(1018)^2 = 1036324, last digit = 4
N = 3
(1018)^3 = 1054977832, last digit = 2
'''
# SOLUTION - 21/8/2021 9:07PM
for _ in range(int(input())):
  digits = [6, 8, 4, 2]
  num = int(input())
  if num == 0: print(1)
  else: print(digits[num%4])
