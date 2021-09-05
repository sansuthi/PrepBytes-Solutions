# Floor of a Number
'''
We all have learnt about floor of a number in school. Let us try and frame a problem statement around that. So, you are given a number 
x and a sorted array A containing N distinct integers. Your task is to find floor of x in the array A(0-based indexing). Now you might be 
wondering what will be floor of x in A? Let me tell you, the floor of x will largest element in A that is smaller than or equal to x.

Input format
First line contains an integer T, number of test cases. Then follows T test cases. Each test case consists of two lines.
First line contains N and x.
Second lines contains N space separated integers.

Output format
Print T lines, each containing index of the floor of x if it exists else print −1.

Constraints
. 1 <= T <= 10^6
. 1 <= N <= 2.5∗10^6
. 0 <= A[i] <= 2∗10^6

Example
Input
3
7 0
1 2 8 10 11 12 19
7 5
1 2 8 10 11 12 19
7 10
1 2 8 10 11 12 19

Output
-1
1
3
'''
# SOLUTION - 31/8/2021 11:26AM
for _ in range(int(input())):
  N, x = map(int, input().split())
  floor = len([int(n) for n in input().split() if int(n) <= x])
  print(-1) if floor == 0 else print(floor-1)