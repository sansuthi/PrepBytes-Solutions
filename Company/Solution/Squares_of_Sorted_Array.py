# Squares of Sorted Array
'''
You are given an array A of N integers, sorted in non-decreasing order. The task is to determine the squares of each number, 
also sorted in non-decreasing order.
Note: You need to solve in constant space, without using the sort() function.

Input Format
The first line of input contains a single integer T - denoting the number of test cases.
Each test case follows:
The first line of each test case contains a single integer N - denoting the number of elements in the array.
The second line contains N space-separated integers - denoting elements of the array.

Output Format
Print the N space-separated integers in non-decreasing order, denoting the square of each element. 
Display the answer for each test case in a separate line.

Constraints
. 1 ≤ T ≤ 100
. 1 ≤ N ≤ 10^4
. −10^4 ≤ Ai ≤ 10^4

Examples
Input
2
5
-3 -2 0 4 9
4
-1 0 1 2

Output
0 4 9 16 81
0 1 1 4
'''
# SOLUTION - 10/9/2021 9:24PM
for _ in range(int(input())):
  n, new = input(), []
  array = [int(a)**2 for a in input().split()]
  for i in range(len(array)):
    minimum = min(array)
    new.append(minimum)
    array.remove(minimum)
  print(*new)
