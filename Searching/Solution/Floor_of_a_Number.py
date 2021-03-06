# Floor of a Number
'''
We all have learnt about floor of a number in school. Let us try and frame a problem statement around that. 
So, you are given a number x and a sorted array A containing N distinct integers. Your task is to find floor 
of x in the array A(0-based indexing). Now you might be wondering what will be floor of x in A? Let me tell you, 
the floor of x will largest element in A that is smaller than or equal to x.

Input format
First line contains an integer T, number of test cases. 
Then follows T test cases. Each test case consists of two lines.
First line contains N and x.
Second lines contains N space separated integers.

Output format
Print T lines, each containing index of the floor of x if it exists else print −1.

Constraints
. 1 <= T <= 10^6
. 1 <= N <= 2.5∗10^6
. 0 <= A[i] <= 2∗10^6

Time Limit
1 second

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
# SOLUTION - 29/3/2022 3:18PM
for _ in range(int(input())):
  N, x = map(int, input().split());
  A = list(map(int, input().split()));
  index = -1; i = N-1;
  while i >= 0:
    if A[i] <= x:
      index = i;
      break;
    i -= 1;
  print(index);
