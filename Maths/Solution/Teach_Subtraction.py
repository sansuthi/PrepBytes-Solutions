# Teach Subtraction
'''
Harry is teaching his 5-year-old son, ShinChan, Subtraction. But ShinChan does it wrong with a number consisting of two or more digits.
He subtracts one from a number by the following algorithm -
. If the last digit of the number is non-zero, he decreases the number by one.
. If the last digit of the number is zero, he divides the number by 10 (i.e. removes the last digit).
You are given an integer N. ShinChan will subtract one from it, K times. The task is to print the result after all K subtractions.

Input Format
The first line of input contains a single integer T - denoting the number of test cases.
The only line of each test case contains two space-separated integers - N and K.

Output Format
Print the result after subtracting 1 from N, K times. Display answer for each test case in a new line.

Constraints
. 1 ≤ T ≤3
. 2 ≤ N ≤ 10^9
.1 ≤ K ≤ 50

Examples
Input
2
512 4
1000000000 9

Output
50
1
'''
# SOLUTION - 17/8/2021 12:41PM
for _ in range(int(input())):
  number, limit = map(int, input().split())
  for i in range(limit):
    if number % 10 == 0:
      number //= 10
    else:
      number -= 1
  print(number)
