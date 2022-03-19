# First Capital Using Recursion
'''
A string T consisting of both lowercase and uppercase English alphabets, find out the position of the first capital 
(uppercase) alphabet present in T(0-based indexing) recursively.

Input format
The first line contains an integer N, representing the number of test cases.
Each test case contains one string T.

Output format
For each test case on a new line, print the position of the first uppercase alphabet, if the string doesn't 
contain any uppercase alphabet than print −1.

Constraints
. 1 <= N <= 100
. 1 <= |T| <= 10^4, where |T| represents the length of the given string.

Time Limit
1 second

Example
Input
2
prepBytes
algorithM

Output
4
8
'''
# SOLUTION - 19/3/2022 8:05PM
def first_capital(string, index):
  if len(string) == 0:
    return -1
  elif string[0].isupper():
    return index
  else:
    return first_capital(string[1:], index+1)
  
for _ in range(int(input())):
  print(first_capital(input(), 0))
