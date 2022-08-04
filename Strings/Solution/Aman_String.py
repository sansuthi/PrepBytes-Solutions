# Aman String
'''
Aman has string str, consisting of lowercase English alphabets. He wants to find the number of such pairs of indices 
(i,j)(1 ≤ i ≤ j ≤ |str|) such that string S(i,j) contains at least once the string aman as a substring.

Input Format
The first line contains an integer T, denoting the number of test cases.
Each test case contains a non-empty string of str.

Output  Format
Print a single number — the answer to the problem.

Constraints
. 1 ≤ T ≤ 10
. 1 ≤ |str| ≤ 10^3, where |str| represents the length of the string.

Time Limit
1 second

Examples
Input
2
amanmgnaa
amanaaamanc

Output
6
20

Explanation of sample test cases.
In the first sample, the following pairs 
(i,j) match: (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9).

In the second sample, the following pairs 
(i,j) match: (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 10), 
(2, 11), (3, 10), (3, 11), (4, 10), (4, 11), (5, 10), (5, 11), (6, 10), (6, 11), (7, 10), (7, 11).
'''
# SOLUTION - 2/8/2022 10:12AM	
for T in range(int(input())):
  string = input();
  count = 0;
  for i in range(len(string)-1):
    for j in range(i, len(string)):
      if 'aman' in string[i:j+1]:
        count += 1;
  print(count);
