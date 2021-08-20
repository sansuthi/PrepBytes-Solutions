# Return Back
'''
You are given a string S which represents the movement sequence of a Robot. Valid moves are R (right), L (left), U (up), and D (down). 
The robot starts its movement from the origin (0, 0) on a 2D plane. The task is to determine if the robot returns to the origin after 
completing all the moves given in the string S.

Input Format
The first line of input contains a single integer T - denoting the number of test cases.
Each test case contains a string S - denoting the movement sequence.

Output Format
Print "Yes" (without quotes) if the robot returns to the origin. Else print "No" (without quotes). 
Display output for each test case in a new line.

Constraints
. 1 ≤ T ≤ 100
. 1 ≤ |S| ≤ 10^4, where |S| denotes the length of string S.

Examples
Input
3
RRLLUD
RLUD
LULL

Output
Yes
Yes
No
'''
# SOLUTION - 20/8/2021 12:08PM
from collections import Counter
for _ in range(int(input())):
  cnt = Counter(input())
  if cnt['R'] == cnt['L'] and cnt['U'] == cnt['D']: print('Yes')
  else: print('No')
