# Denomination
'''
Arnab is now the cashier of his newly opened business. He has a lot of notes of each denomination
(1,2,5,10,20,50,100,500,1000). He has to pay his customer a change of N rupee. Find him the minimum 
number of denominations required to pay back the change.

Input format
. First-line contains an integer T where T is the number of test cases.
. For every Test case: The next line contains N. 

Output format
For every test case print the minimum number of denominations required to pay back the change in a new line. 

Constraints
. 1 <= T <= 70
. 1 <= N <= 10^5

Time Limit
1 second

Example
Input
5
35
24
100
90
23

Output
3
3
1
3
3
'''
# SOLUTION - 13/6/2022 12:11PM
for _ in range(int(input())):
  N = int(input());
  D = [1000,500,100,50,20,10,5,2,1];
  count = 0;
  for d in D:
    count += N//d;
    N %= d;
  print(count);
