# Leap Year or Not
'''
We all have made fun of our friends who have their birthdays on 29th February.
Given birthday year N of your friend, can you tell her if that is leap year or not? 

Input format
The first line constains an integer T denoting the number of test cases.
Each test case contains one integer N.

Output format
For each test case on a new line, print Yes if the given year is a leap year else print No.

Constraints
. 1 <= T <= 10
. 1 <= N <= 2500

Example
Input
2
1900
2012

Output
No
Yes
'''
# SOLUTION - 30/8/2021 12:41PM
for _ in range(int(input())):
  year = int(input())
  if (year%400 == 0 or (year%4 == 0 and year%100 != 0)): print('Yes')
  else: print('No')
