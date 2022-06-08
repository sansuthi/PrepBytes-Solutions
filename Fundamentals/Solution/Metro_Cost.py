# Metro Cost
'''
Himanshu travels N times in Delhi metro daily. One normal ride of metro costs p rupees, 
a special ticket with price q is also available that lets Himanshu take S out of N rides at q price.

Help Himanshu to find what is the minimum sum of money he will have to spend to complete N rides.

Input format
. First line contains test case T.
. T test cases follow,The one and only line contain four space-separated integers N,S,p,q.

Output format
For each test case, print the minimum amount of money needed to complete N rounds

Constraints
. 1 <= T <= 10^2
. 1 <= N,S,p,q <= 10^3

Time Limit
 1 second

Example
Input
1
6 4 1 3

Output
5

Sample test case explanation
N=6, S=4, p=1, q=3
4 rides can be done in 3 rupees and remaining 2 rides can be completed in 1 rupee each, 
so in total 3+1+1 = 5.
'''
# SOLUTION - 8/6/2022 1:25PM
for _ in range(int(input())):
  N, S, p, q = map(int, input().split());
  if N > S:
    if q < p:
      price = (N//S)*q;
      if (N%S)*p < q:
        price += (N%S)*p;
      else:
        price += q;
    else:
      p1 = ((N//S)*q) + ((N%S)*p);
      p2 = N * p;
      price = min(p1, p2);     
  else:
    if N*p < q:
      price = N*p;
    else:
      price = q;
  print(price);
