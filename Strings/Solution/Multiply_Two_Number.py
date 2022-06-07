# Multiply Two Number
'''
You guys know how to multiply two numbers. This time PrepBuddy decide to give two strings 
S1 and S2, both strings contain non-negative integers. PrepBuddy asks you to print the product of 
S1 and S2.The output will be also represented as a string.

Note: 
Both S1 and S2 contain only digits 0−9.
Both S1 and S2 do not contain any leading zero, except the number 0 itself.

Input Format
. The first line contains an integer T, denoting the number of test cases.
. Each test case contains two strings S1 and S2.

Output  Format
Print the product of S1 and S2.

Constraints
. 1 ≤ T ≤ 10^2
. 1 ≤ |S1|,|S2| ≤ 10^2; where |S1|, |S2| represent length of the strings. 

Time Limit
1 second

Example:
Input
2
3 2
12 10

Output
6
120
'''
# SOLUTION - 7/6/2022 10:50AM
for _ in range(int(input())):
  S1, S2 = input().split();
  prod = str(int(S1)*int(S2));
  print(prod);
