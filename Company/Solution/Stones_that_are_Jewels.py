# Stones that are Jewels
'''
You are given two strings - S representing the types of stones that are jewels, and P representing the stones you have.
The task is to determine how many stones you have which are also jewels.

Input Format
The first line of input contains a single integer T - denoting the number of test cases.
Each test case contains two strings S and P.

Output Format
Print the number of stones you have which are also jewels. Print answer for each test case in a new line.

Constraints
. 1 ≤ T ≤ 10^2
. 1 ≤| S|, |P| ≤ 10^4, where |S| and |P| denotes the length of the string S and P.
The letters in S are guaranteed distinct

Examples
Input
2
zZ zaZz
abc Abc

Output
3
2

Sample Test Case Explanation
For first test case:
The jewels are - 'Z', 'z'
Stones which are also jewels in "zaZz" - 'z', 'Z', 'z'
Answer = 3

For second test case:
The jewels are - 'a', 'b', 'c'
Stones which are also jewels in "Abc" - 'b', 'c'
Answer = 2
'''
# SOLUTION - 10/9/2021 2:27PM
for _ in range(int(input())):
  S, P = input().split()
  print(sum([1 for p in P if p in S]))
