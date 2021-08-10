# Product Array
'''
You are given an array A of N integers. For every element, you need to return the product of the array except that element.
Note: You need to do without using the division operator and in O(n).

Input Format
. First-line contains a single integer T -denoting the number of test cases.
. First line of each test case contains a single integer N.
. Second line of each test case contains N space-separated integers-denoting the elements of the array.

Output Format
For each testcase print a N space-separated integers where the ith integer denotes the product of the array except that integer.

Constraints
. 1 <= T <= 100
. 1 <= N <= 20
. 1 <= Ai <= 10

Examples
Input
2
5
1 2 3 4 5
4
8 7 6 5

Output
120 60 40 30 24 
210 240 280 336 
'''
# SOLUTION - 10/8/2021 10:07PM
from itertools import accumulate
for _ in range(int(input())):
  n = input()
  array = list(map(int, input().split()))
  product = [*accumulate(array, lambda a, b: a*b)][-1]
  print(*[product//i for i in array])
