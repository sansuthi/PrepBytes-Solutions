# Multiplication of Digits
'''
Given an integer N, recursively find the multiplication of digits of N modulus with 10^9 + 7.

Input format
The first line contains an integer T, representing the number of test cases.
Each test case contains one integer N.

Output format
For each test case on a new line, print the required multiplication modulus 10^9 + 7.

Constraints
. 1 <= T <= 100
. 1 <= N <= 10^18

Time Limit
1 second

Example
Input
2
123
4567

Output
6
840
'''
# SOLUTION - 19/3/2022 9:33PM
def digit_mul(num, product=1):
    if len(num) == 0:
        return product % ((10**9)+7)
    else:
        return digit_mul(num[1:], product*int(num[0]))

for _ in range(int(input())):
    print(digit_mul(input().strip()))
