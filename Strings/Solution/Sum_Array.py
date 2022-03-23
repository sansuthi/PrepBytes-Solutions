# Sum Array
'''
Given an array of n integers find the sum of all the elements of the array.
Note: the elements of the array might be large.

Input format
First line contains integer t, denoting the number of testcases. 
For each testcase:
First line contains an integer n.
Second line contains n space separated integers.

Output format
For each testcase print the sum of all the array elements on a new line.

Constraints
. 1 <= t <= 50
. 1 <= n <= 10^2
. 1 <= arr[i] <= 10^100

Time Limit
1 second

Example
Input
2
3 
10 20 30
4 
100 600 320 10

Output
60
1030
'''
# SOLUTION - 23/3/2022 3:16PM
for _ in range(int(input())):
  N = int(input());
  array = list(map(int, input().split()));
  arr_sum = 0;
  for i in range(N):
    arr_sum += array[i];
  print(arr_sum);
