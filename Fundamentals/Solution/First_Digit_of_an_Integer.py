# First Digit of an Integer
'''
We already saw how to find the last digit of a number. Let's proceed ahead with finding the first digit. 
Given a four-digit number N, find its first digit. There will be no leading zeros in the integer N.

Input format
The first line contains an integer T denoting the number of test cases.
Each test case contains one integer N.

Output format
For each test case on a new line, print the first digit of N.

Constraints
. 1 <= T <= 10
. 1000 <= N < 10000

Time Limit
1 second

Example
Input
2
1234
4567

Output
1
4

Sample Test case Explanation
First digit of integer 1234 is 1.
First digit of integer 4567 is 4.
'''
# SOLUTION - 20/3/2022 10:09PM
for _ in range(int(input())):
  number = int(input())
  while (number >= 10):
    number //= 10
  print(number)
