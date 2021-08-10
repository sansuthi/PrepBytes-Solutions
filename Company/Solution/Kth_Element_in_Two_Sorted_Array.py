# Kth Element in Two Sorted Array
'''
You are given two sorted array A and B of length N and M. You need to find the Kth element of the final sorted array.
Note: You need to do in O(logK) time complexity and O(1) space complexity.

Input Format
. First line contains a single integer T -denoting the number of test cases
. First line of each test case contains three integers N, M and K.
. Second line of each testcase contains N space separated integers-denoting the elements of the first array.
. Third line  each testcase contains M space separated integers -denoting the elements of the second array.

Output Format
Print a single integer denoting the Kth element of the final sorted array. 

Constraints
. 1 <= T <= 100
. 1 <= N, M <= 10^6
. 1 <= Ai, Bi <= 10^6
. 1 <= K <= N + M

Examples
Input
2
3 4 3
1 4 7 
5 6 8 9
6 5 7
7 8 15 17 19 20
1 7 20 21 22

Output
5
19

Explanation
For the first testcase:
The 3rd element will be 5 in 1 4 5 6 7 8 9 
'''
# SOLUTION - 31/7/2021 10:27PM
  N, M, K = map(int, input().split())
  n = list(map(int, input().split()))
  m = list(map(int, input().split()))
  print(sorted(n+m)[K-1])
