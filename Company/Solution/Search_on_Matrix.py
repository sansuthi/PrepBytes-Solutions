# Search on Matrix
'''
You have already familiar with the search on a sorted array, But can you search an element in a sorted 2D matrix? By sorted matrix. 
This 2D matrix has 2 properties
1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.
You will be given an N∗M matrix and a value X to be searched in it if it is present in the matrix print "Yes" otherwise "No".
Note: your search algorithm should have a time complexity = O(log(N∗M)). 

Input format:
First input line will be consists of three space separated integers N and M, X representing the number of rows,  number of columns 
and the value to be searched respectively. Next N lines will be consists of M space separated integers.

Output format:
If X is present in the matrix print "Yes" otherwise "No".

Constraints:
. 1 <= N, M <= 10^3
. 1 <= a[i][j] <= 10^9

Example:
Input
3 3 5
1 2 3
4 5 6
8 10 15

Output
Yes
'''
# SOLUTION - 22/8/2021 2:01PM
n, m, x = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
for ar in array: 
  if x in ar:
    print('Yes')
    break
else: print('No')
