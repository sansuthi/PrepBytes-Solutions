# Vowels and Consonants
'''
Let's take a simple problem. We all know what are vowels and consonants. Your task is pretty simple, 
given a string S, count number of vowels and consonants present in the string.

Input format
The first line contains an integer T, denoting the number of test cases.
Each test case consists of a string S containing only uppercase characters.

Output format
For each test case on a new line, print vowel count and consonant count separated by a space.

Constraints
. 1 <= T <= 15
. 1 <= |S| <= 10^7, where |S| denotes length of string S.

Time limit
1 second

Example
Input
2
PREPBYTES
FLY

Output
2 7
0 3
'''
# SOLUTION - 23/3/2022 12:53AM
for _ in range(int(input())):
  count = [0, 0];
  string = input();
  for letter in string:
    if letter in 'AEIOU':
      count[0] += 1;
    else:
      count[1] += 1;
  print(*count);
