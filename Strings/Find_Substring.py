# Find Substring
'''
A substring is a contiguous sequence of characters within a string. PrepBuddy gave you two string s and t and ask you to check 
string t is a substring of s or not. If string t is a substring of s then print "YES" otherwise Print "NO" without quotes.

Example: 
s=prepbytes, t=prep
here-string t is Substring of string s.
Note: Both string contains lowercase English letters

Input Format
The first line contains an integer T, that represent the number of test cases.Each test-cases contains two string s and t. 

Output
If string t is Subtring of string s then print "YES" otherwise Print "NO" withou quote.

Constraints
1 ≤ T ≤ 10
1 ≤ |s|,|t| ≤ 10^3  
|s|,|t| is length of string.

Input
2
prepbytes prep
abcd efgh

Output
YES
NO
'''
# SOLUTION - 31/7/2021 1:36AM
for _ in range(int(input())):
  s, t = input().split()
  print('YES') if t in s else print('NO')
