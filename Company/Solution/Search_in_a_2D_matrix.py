# Search in a 2D matrix
'''
Given a N * M matrix, and a value K find if K exists in the matrix or not.

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Note: Use binary Search to solve the problem.

Input format
First line contains N and M and K denoting rows, columns and the number which has to be searched.
Each of next N line contains M space separated integers

Output format
Print 1 if element is found otherwise 0

Constraints
. 1 <= N, M <= 500
. 1 <= K, matrix[i][j] <= 100000

Example
Input
3 4 3
1 3 5 7
10 11 16 20
20 30 34 50

Output
1

Explanation:
3 is present in the matrix
'''
# SOLUTION - 22/8/2021 3:06PM
n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
if k in sum(array, []): print(1)
else: print(0)
