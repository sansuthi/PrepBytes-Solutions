# Min and Max
'''
Congratulations on making up to this question. Let us give you a fairly simple array problem to solve.  
If you know how to iterate through the array, you will easily be able to solve this. The problem statement 
is simple- given N elements, find the minimum and maximum numbers among those elements.

Input format
The first line contains test case T denoting the number of test cases.Each test case consists of two lines,
First-line contains N representing the length of the array. The second line contains N space-separated integers.

Output format
For each test case on a new line, print minimum and maximum elements separated by space.

Constraints
. 1 <= T <= 5
. 1 <= N < 10^7
. 0 <= A[i] <= 10^7

Time limit
1 second
 
Example
Input
2
6
3 1 4 6 2 7
6
0 0 0 0 0 0
 
Output
1 7
0 0

Sample Test Case Explanation
In the first test case, minimum element = 1 and maximum element = 7
In the second test case, minimum element = 0 and maximum element = 0
'''
# SOLUTION - 9/4/2022 12:15PM
for _ in range(int(input())):
  N = int(input());
  A = list(map(int, input().split()));
  minimum = maximum = A[0];
  for i in range(1, N):
    if A[i] < minimum:
      minimum = A[i];
    if A[i] > maximum:
      maximum = A[i];
  print(minimum, maximum);
