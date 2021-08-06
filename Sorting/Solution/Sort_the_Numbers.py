# Sort the Numbers
'''
Some problems are like a mirage. They seem to have a different solution when you see it first but as you 
deep dive you realize the solution is something else. Next, we are going to solve one such problem.
You are given an array consisting of 0's, 1's and 2's. Your task is to sort the array.

Input Format
The first line contains an integer T, number of test cases. Then follows T test cases. Each test case consists of two lines.
The first line contains N, size of the array.
Second line contains N space-separated positive integers A[i] denoting elements of the array.

Output Format
The output contains T lines, each printing the sorted array.

Constraints
1 <= T <= 100
1 <= N <= 5∗10^5
A[i] = 0|1|2

Example
Input
2
10
0 1 0 0 1 0 2 2 0 1 
10
2 2 2 2 2 1 1 2 0 2

Output
0 0 0 0 0 1 1 1 2 2 
0 1 1 2 2 2 2 2 2 2
'''
# SOLUTION - 2/8/2021 10:11PM
for _ in range(int(input())):
  n = input()
  array = [int(x) for x in input().split()]
  print(*sorted(array))
