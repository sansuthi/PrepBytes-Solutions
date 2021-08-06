# Anagram or Not
'''
A string T is said to be an anagram of a string S if it is created by rearranging the characters which are present in string S.
PrepBuddy has a string S and Tina has a string T, they want to know whether S and T are an anagram of each other or not.

Input format
The first line contains an integer N, representing the number of test cases. Each test case contains two strings S and T separated by a line.

Output format
For each test case on a new line, print YES if S and T are an anagram of each other else print NO.

Constraints
1 <= N <= 100
1 <= |S| = |T| <= 10^4, where |S| and |T| represents the length of the given strings.

Example
Input
2
prep
pepr
abcd
efgh

Output
YES
NO

Sample test case explanation
In the first test case both the string contains the same characters [p,r,e,p], therefore, the output is YES.
'''
# SOLUTION - 31/7/2021 1:32AM
for _ in range(int(input())):
  print('YES') if sorted(input()) == sorted(input()) else print('NO')
