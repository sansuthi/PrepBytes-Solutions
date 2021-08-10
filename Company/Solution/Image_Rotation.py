# Image Rotation
'''
An image has been provided to you which can be represented by a matrix of rows and columns. 
You need to rotate the image by 90 degrees (clockwise).

Follow Up: Do it in O(1) space.

Input Format
. First line of input contains two integers N and M - denoting the number of rows and columns.
. N line follows having M space separated integers

Output Format
Print the resultant image

Constraints
. 0 < N < 1000
. 0 < M < 1000

Examples
Input
3 3
3 6 9 
2 5 8 
1 4 7 

Output
1 2 3 
4 5 6 
7 8 9 
'''
# SOLUTION - 10/8/2021 12:39PM
m, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(m)]
array.reverse()
for i in range(m):
    for ar in array:
        print(ar[i], end=' ')
    print()
