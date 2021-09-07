# Smallest Lexicographic String
'''
Sahil knows the dictionary order of letters. But his teacher changed the order of the letters in the dictionary. And his teacher said that to 
use the new dictionary to find the smallest lexicographical string. His teacher gave him two strings D and S, D denotes the new order of letters 
in the English dictionary. His teacher asked him to find the smallest lexicographic string made from the given string S.

Input Format:
First-line contains an integer T, denoting the number of test cases.For each test case:-
First-line contains a string D.
Second-line contains a string S.

Output Format:
For each test case, print the output on a new line, the smallest lexicographic string made from the given string S.

Constraints:
. 1 <= T <= 10^3
. 1 <= D <= 26
. 1 <= S <= 10^2

Example
Input
2
mbjyalzvepsfonxqgduritwkch
cbmaz
tzechoqkpbujirsdnvxmlygwaf
prepbytes

Output
mbazc
teeppbrsy
'''
# SOLUTION - 7/9/2021 10:49PM
for _ in range(int(input())):
  letters, string, new = input(), input(), ''
  for letter in letters:
    new += letter*string.count(letter)
  print(new)
