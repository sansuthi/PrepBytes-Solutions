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
# SOLUTION - 22/3/2022 12:34PM	
for _ in range(int(input())):
  v_count = 0; c_count = 0;
  string = input().lower();
  for letter in string:
    if letter in 'aeiou':
      v_count += 1;
    else:
      c_count += 1;
  print(v_count, c_count);
