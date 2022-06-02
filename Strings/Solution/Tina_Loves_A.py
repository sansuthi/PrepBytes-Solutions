# Tina Loves A
'''
Tina has a string S. She really likes the letter a. She calls a string good if strictly 
more than half of the characters in that string are a's. For example "aaacb", "acaa" 
are good strings, and "baba", "abbba"," "(empty string) are not.

Tina can erase some characters from her string S. She would like to know what is the length of the 
longest string remaining after erasing some characters (possibly zero) to get a good string. It is 
guaranteed that the string has at least one a in it, so the answer always exists.

Input format
. The first line contains an integer T, denoting the number of test cases.
. Each test case consists of a string S containing only lowercase characters.

Output format
For each test case on a new line, print the length of longest good string.

Constraints
. 1 <= T <= 10
. 1 <= |S| <= 10^7, where |S| denotes length of string S.

Time limit
1 second

Example
Input
2
xaxxxxa
aaabaa

Output
3
6
'''
# SOLUTION - 2/6/2022 9:01PM
for _ in range(int(input())):
  string = input();
  a_count = string.count('a');
  not_a = len(string) - a_count;
  while a_count <= not_a:
    not_a -= 1;
  print(a_count + not_a);
