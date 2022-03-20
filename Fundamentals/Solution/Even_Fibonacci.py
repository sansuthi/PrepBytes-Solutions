# Even Fibonacci
'''
PrepBuddy wants you to find the Nth Even Fibonacci number. 
Since the answer can be very large, print the answer modulo 1000000007.

Input format
The first line of input contains T denoting the number of test-cases. 
Then each of the T lines contains a single positive integer N.

Output format
Output the Nth Even Fibonacci number.

Constraints
. 1 <= T <= 100
. 1 <= N <= 10^3

Time Limit
1 second

Example
Input
3
1
2
5

Output
2
8
610
'''
# SOLUTION - 20/3/2022 11:00PM	
for _ in range(int(input())):
    first = 0; second = 1
    i = int(input())
    while i != 0:
        number = first + second
        first = second
        second = number
        if number % 2 == 0:
            i -= 1
    print(number%1000000007)
