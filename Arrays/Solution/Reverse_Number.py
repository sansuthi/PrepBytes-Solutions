# Reverse Number
'''
You have given an array that contains N numbers. You have to print those numbers in reverse order.

Input Format
The first line contains an integer N, N represents the number of elements present in the array. 
The second line contains N numbers separated by spaces.

Output Format
Print the array in reverse order.

Constraints
. 1 <= N <= 10^3
. 1 <= arr[i] <= 10^3

Time Limit
1 second

Input
5
1 2 3 4 5

Output
5 4 3 2 1

Sample test case explanation
arr[] = [1,2,3,4,5]
o/p = [5,4,3,2,1]
'''
# SOLUTION - 21/3/2022 5:30PM
N = int(input()) - 1
arr = list(map(int, input().split()))
while N != -1:
    print(arr[N], end=' ')
    N -= 1
