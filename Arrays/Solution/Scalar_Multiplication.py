# Scalar Multiplication
'''
You are given a M∗N matrix, and a variable K, print the resultant matrix after scalar multiplication.

Input format
First line contains M, N and K representing rows, columns and scalar.
Each of the next M lines contains N integers.

Output format
Print the resultant matrix.

Constraints
. 1 <= M,N <= 5
. 1 <= K <= 100

Time limit
1 second

Example
Input
2 2 5
1 2
3 4

Output
5 10
15 20
'''
# SOLUTION - 21/3/2022 4:57PM
m, n, x = map(int, input().split())
for i in range(m):
    array = list(map(int, input().split()))
    for j in range(n):
        print(array[j] * x, end=' ')
    print()
