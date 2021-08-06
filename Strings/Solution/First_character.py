# First character
'''
Prepbuddy has a string S consisting of lowercase Latin Letters. The String S can contain some repeated characters, no repeated 
characters, and maybe all repeated characters. He is trying to find the first character which is non-repeating in S. The String 
S contains many non-repeating characters, so he is not able to find the answer. You can help him to find the answer. 

Note:- Print −1 if there is no non-repeating character.

Input Format
The first line contains T denoting the number of test cases. 
Then following each test case, the next line contains the string S.

Output Format
For each test case, print the index of the first non-repeating character present in the string. 
Print −1 if there is no non-repeating character.

Constraint
. 1 <= T <= 900
. 1 <= |S| <= 10^4, where |S| denotes the length of string S. 

Example
Input
3
hello
zxvczbtxyzvy
xxyyzz

Output
0
3
-1

Sample test case Explanation
In the first test case.
'h', 'e', and 'o' are non-repeating characters, but the character 'h' is the first non-repeating. 
So the answer is the index of 'h'.
Output: 0

In the second test case 
'z' is present at the index 0,4 and 9
'x' is present at the index 1 and 7 
'v' is present at the index 2 and 10
'c' is present only at index 3, so 3 is the output.
'b' is present only at index 5, so 5 is the output
't' is present only at index 6, so 6 is the output

'c', 'b', and 't' are non-repeating characters, but the character 'c' is the first non-repeating. that's why 'c' is the answer.
Output: 3
'''
# SOLUTION - 6/8/2021 3:02PM
for _ in range(int(input())):
  string = input()
  for st in string:
    if string.count(st) == 1:
      print(string.index(st))
      break
  else:
    print(-1)
