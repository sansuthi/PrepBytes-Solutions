# Missing in AP
'''
Arithmetic expression was an interesting concept that we learned in maths. What about solving a problem around that. 
Let's say I give you N elements and I tell you that the elements are representing AP(Arithmetic Progression). But you 
realize that one element from this AP is missing and you want to find out the missing element. It is easy to find out 
the missing one for a human but can you write down a program that does this task of finding a missing element from the AP?

Input format
First line contains an integer T, number of test cases. Then follows T test cases. Each test case consists of two lines.
First line contains N.
Second lines contain N space separated integers.

Output format
Print T lines, each line containing the missing element.

Constraints
. 1 <= T <= 10
. 3 <= N < 2∗10^6
. 1 <= A[i] <= 10^7+5

Time Limit
1 second

Example
Input
2
5
1 4 10 13 16
5
1 5 9 17 21

Output
7
13
'''
# SOLUTION - 29/3/2022 3:30PM
for _ in range(int(input())):
  N = int(input());
  A = list(map(int, input().split()));
  diff = A[-1] - A[-2];
  for i in range(N-1):
    if A[i+1] - A[i] != diff:
      missing = (A[i+1] + A[i])//2;
      break;
  print(missing);
