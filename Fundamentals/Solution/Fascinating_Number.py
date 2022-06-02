# Fascinating Number
'''
PrepBuddy find any four digit number fascinating that has all the 4 digits unique. 
For example 1234 is a fascinating number. His friend Rahul gave him N numbers and asks him to 
find the minimum number which is strictly larger than the given one and has only distinct digits.

Input format
. The first line of the input contains integer N, denoting the count of numbers provided by Rahul.
. Each of the next N lines contains one integer.

Output format
Print the next fascinating number.

Constraints
. 1 <= N <= 10
. 1000 <= number <= 9000

Time Limit
1 second

Example
Input
2
1234
2010

Output
1235
2013

Sample test case explanation
1235 is the minimum number that is larger than 1234 with all 4 digits 1,2,3,5 distinct.
'''
# SOLUTION - 2/6/2022 6:27PM
for _ in range(int(input())):
  number = int(input());
  flag = False;
  while not flag:
    number += 1;
    temp = number;
    fs = temp % 10;
    temp //= 10;
    sc = temp % 10;
    temp //= 10;
    th = temp % 10;
    temp //= 10;
    fr = temp % 10;
    temp //= 10;
    if fs != sc and fs != th and fs != fr:
      if sc != th and sc != fr:
        if th != fr:
          flag = True;
  print(number);
