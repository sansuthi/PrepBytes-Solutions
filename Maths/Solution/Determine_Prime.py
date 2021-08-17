# Determine Prime
'''
Given a number N, your task is to print "Yes" if N is prime number else print "No".

Input format
First line contains an integer T, representing the number of test cases.
For each of the next T lines, each line contains an integer N.

Output format
For each test case on a new line, print "Yes"(without quotes) or "No"(without quotes) depending on N.

Constraints
. 1 <= T <= 50
. 1 <= N <= 10^6

Example
Input
2
53
8

Output
Yes
No
'''
# SOLUTION - 17/8/2021 12:21PM
for _ in range(int(input())):
    number = int(input())
    flag = False
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
    print('No') if flag else print('Yes')
