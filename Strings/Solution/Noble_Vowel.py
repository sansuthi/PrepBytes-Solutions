# Noble Vowel
'''
Given a string S your task is to find out whether a string is Noble Vowel string or not. 
A Nobel Vowel string is one in which there has to be a vowel after every consonant, 
but there can be any letter after any vowel. The only exception is a consonant n; 
after this letter, there can be any letter (not only a vowel) or there can be no letter at all.

Input format
. The first line contains an integer T denoting the number of test cases.
. Each test case consists of one string S consisting of lower case alphabets.

Output format
For each test case on a new line print YES if S is a Noble Vowel string else print NO.

Constraints:
. 1 <= T <= 10
. 1 <= |S| <= 1000

Time Limit
1 second

Example
Input
2
aeiou
cefduo

Output
YES
NO

Explanation
In the first string, every vowel is followed by another vowel or consonant. 
So the string is Noble Vowel.
In the second string, f is a consonant, which should be followed by a vowel 
but it is being followed by another consonant, so this string is not Noble Vowel.
'''
# SOLUTION - 7/6/2022 10:41AM
for _ in range(int(input())):
  S = input() + ' ';
  vowels = 'aeiou'; 
  result = 'YES'; 
  for i in range(len(S)-1):
    if S[i] not in vowels and S[i] != 'n':
      if S[i+1] not in vowels:
        result = 'NO';
        break;
  print(result);
