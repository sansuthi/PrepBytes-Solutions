# Frequency of characters
'''
You are given a string S of length N containing only small letters alphabets. You are also given an integer Q, denoting the number of queries. 
For each query you are given an integer i(1<=i<=N) denoting the ith position character in the string S. You have to find the character present 
at index i and print the frequency of the same character preceding the given i position.

Input Format
The first line contains a string S.
The second line contains an integer Q, denoting the number of queries.
Next Q lines contain a single integer i, denoting the position of a character. 

Output Format
For each query, print a single integer. The frequency of ith position character preceding the given i position.

Constraints
. 1 <= N <= 5∗10^5
. 1 <= Q <= 10^4

Example
Input
acsaacahfc
2
7
10

Output
3
2
'''
# SOLUTION - 7/9/2021 10:21PM
string = input()
for _ in range(int(input())):
  index = int(input())-1
  print(string[:index].count(string[index]))
