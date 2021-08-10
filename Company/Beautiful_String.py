# Beautiful String
'''
Claudia is playing with strings. She has two strings and she wanted both of them to be beautiful. 
According to Claudia both the strings are beautiful if one of the string is a permutation of the other.
You need to tell if they are beautiful or not.

Input Format
. First line contains a single integer T - denoting the number of test cases.
. Each testcase contains two string S and P.

Output Format
Print "YES" (without quotes) if the given strings are beautiful else print "NO" (without quotes). 

Constraints
. 1 <= T <= 100
. 1 <= |S|, |P| <= 10^5

Examples
Input
2
prepbytes bytesprep
jgec cgec

Output
YES
NO
'''
# SOLUTION - 31/7/2021 10:18PM
for _ in range(int(input())):
  a, b = list(input().split())
  print('YES') if sorted(a) == sorted(b) else print('NO')
