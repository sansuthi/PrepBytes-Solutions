# Majority Votes
'''
There is a voting for class monitor in Tina's class. There were several candidates each having an 
integer voting Id using which students would vote them. Students are done with voting and all the 
votes are kept in an array. Now, Tina is given the task of declaring who won the election. 

The rules are a bit different here, let's say total number of votes are N and for a candidate to 
win she/he should have received more than N/2 votes. Tina has written the most efficient code for this. 
Can you also try and write efficient code for this problem?

Input
First line contains an integer T, number of test cases. 
Then follows T test cases. Each test case consists of two lines.
First line contains N.Second lines contain N space separated integers denoting votes.

Output
Print T lines, each containing the voting Id of the winner. Print −1 if no such winner exists.

Constraints
. 1 <= T <= 10
. 1 <= N <= 5∗10^6
. 1 <= A[i] < 10^6

Time Limit
1 second

Example
Input
2
5
1 3 2 2 2
4
1 3 2 2

Output
2
-1

Sample test case explanation
In the first test case
1. Candidate with voting id = 1 got one vote.
2. Candidate with voting id = 2 got three votes.
3. Candidate with voting id = 3 got one vote.

N=5, so N/2=2, and candidate with voting id = 2 got more than N/2 votes, 
therefore the output is 2
. 
'''
# SOLUTION - 8/6/2022 7:00PM
for _ in range(int(input())):
  N = int(input());
  A = list(map(int, input().split()));
  winner = -1;
  for a in set(A):
    if A.count(a) > N//2:
      winner = a;
  print(winner);
