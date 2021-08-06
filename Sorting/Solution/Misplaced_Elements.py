# Find the misplaced elements
'''
Arnab is given an array of integers of size N. His teacher asked Arnab to sort the array but as usual, 
Arnab did not do his task. So now the teacher will cut his marks for each misplaced element. Arnab wants 
to know how much marks he will lose.

Input format
First-line contains an integer T denoting number of test cases.
For each test case:
The first line contains a number N
The second line contains N integers. 

Output format
For each test case print the answer in a new line.

Constraints:
1 <= t <= 10
1 <= N <= 10^6

Example
Input
1
5
8 4 2 1 9

Output
4

Explanation
So the sorted array is 1,2,4,8,9 and the array we have is 8,4,2,1,9 so the number of misplaced elements is 4.
'''
# SOLUTION - 31/7/2021 2:15PM
for _ in range(int(input())):
  n = input()
  array = list(map(int, input().split()))
  k = sorted(array)
  mis = 0
  for i in range(len(k)):
    if array[i] != k[i]:
      mis += 1
  print(mis)
