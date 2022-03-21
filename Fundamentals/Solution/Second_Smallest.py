# Second Smallest
'''
You are given 3 distinct integer numbers X,Y and Z. 
Task is to print the second smallest number among the three provided numbers.

Input format
Input contains 3 distinct integers X,Y and Z.

Output format
Print the second smallest integer.

Time Limit
1 second

Constraints
. 1 <= X,Y,Z <= 100

Example
Input
10 42 15

Output
15
'''
# SOLUTION - 21/3/2022 12:50PM
n1, n2, n3 = map(int, input().split())
if n1 > n2 and n1 > n3:
  if n2 > n3:
    second = n2
  else:
    second = n3
elif n2 > n1 and n2 > n3:
  if n1 > n3:
    second = n2
  else:
    second = n3
else:
  if n1 > n2:
    second = n1
  else:
    second = n2
print(second)
