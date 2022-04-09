# Students Roll Number
'''
In an examination hall, seat number started from 0 then 1,2,3,.... and so on. English paper and Hindi paper students 
sitting on alternate seats with English paper students starting from seat 0, then Hindi paper student from seat 1 and so on. 
No two students with the same paper will sit together. There are N seats in a single row. Help the examiner to find the roll 
number of only English paper students in a particular row.

Input format
The first line of input contains T denoting the number of test cases. T test cases follow.
Each test case contains two lines of input. The first line contains N and the second line contains the roll number of N students.

Output format
For each test case, print the English paper student's roll number.

Constraints
. 1 <= T <= 10
. 1 <= N <= 10^5
. 1 <= Ai <= 10^5

Time Limit
1 second

Example
Input
2
4
1 2 3 4
5
1 2 3 4 5

Output
1 3
1 3 5
'''
# SOLUTION - 9/4/2022 12:20PM
for _ in range(int(input())):
  N = int(input());
  A = list(map(int, input().split()));
  for i in range(N):
    if i % 2 == 0:
      print(A[i], end=' ');
  print();
