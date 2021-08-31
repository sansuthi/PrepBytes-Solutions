# Find Mountain Top
'''
PrepBuddy wants to climb a mountain this spring. There are different milestones on the mountain represented by 
distinct integer numbers. From bottom to top the milestones are strictly increasing and then from top to bottom, 
they are strictly decreasing. PrepBuddy wants to know the topmost milestone number before starting the journey. 

NOTE - Solve it using Binary Search

Input Format
The first line contains an integer T, denoting the number of test cases.
For each test case: The first line contains an integer N, denoting the number of elements present in the array.
The second line contains N space-separated distinct integers representing the milestone numbers.

Output
For each test case on a new line, print the value of the topmost milestone.

Constraints
. 1 <= T <= 5
. 1 <= N <= 10^5
. 1 <= A[i] <= 2∗10^5

Example
Input
2
7
10 12 14 15 8 7 6
6
10 20 30 4 3 2

Output
15
30

Sample test case explanation
In the first test case, the top most milestone value is 15, after which the values keep on strictly decreasing.
In the second test case, the top most milestone value is 30, after which the values keep on strictly decreasing. 
'''
# SOLUTION - 31/8/2021 1:43PM	
for _ in range(int(input())):
  n = input()
  array = list(map(int, input().split()))
  for i in range(len(array)-1):
    if array[i] > array[i+1]:
      top = array[i]
      break
  print(top)
