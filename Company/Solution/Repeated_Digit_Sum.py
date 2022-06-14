# Repeated Digit Sum
'''
You are given a non-negative integer N. You have to calculate the sum of the digits 
it has repeatedly until the result came down to a single digit. And your task is to 
print that single digit after performing the required operations.

DigitSum(94) = 13 -> DigitSum(13) = 4 which is a single digit so we have to stop here.
Note: Can you do it in O(1) time complexity.

Input format:
The only input line will be consists of an integer N.

Output format:
Print that required single digit.

Constraints:
. 0 <= N <= 10^18

Time limit:
1.0 sec

Example:
Input
94

Output
4
'''
# SOLUTION - 14/6/2022 7:03PM
number = int(input());
loop = True;
while loop:
  digsum = 0;
  while number != 0:
    digsum += number % 10;
    number //= 10;
  if digsum // 10 == 0:
    loop = False;
  else:
    number = digsum;
print(digsum);
