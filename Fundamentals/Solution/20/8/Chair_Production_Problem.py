# Chair Production Problem
'''
Bran has started a Candy shop but he does not have any chairs for his employees. So instead of buying a chair for each employee, 
he decides to manufacture them (costs him 5 Bucks each). Optimally, he starts producing chairs for only those employees who are 
currently idle and needs rest.

Initially, Bran has not produced any of the chairs and asks for your help to find the Minimum Cost of chairs that he needs to 
produce based on a given string A consisting of characters U, M, D, L. 
Each character representing:
. U or M: A new employee becomes idle, if there is a chair available he takes it otherwise Bran produces a new one.
. D or L: An employee starts selling the Candies freeing up a chair.

Input Format
The first line contains T denoting the number of test cases.
The second line contains string A consisting of U, D, M, L.

Output Format
For each test case on a new line, print minimum Cost of Chairs.

Constraints
. 1 ≤ T ≤ 5
. 1 ≤ |A| ≤ 10^5, where |A| represents the length of the string.

Examples
Input
3
UULUM
UUU
LLL

Output
15
15
0
'''
# SOLUTION - 20/8/2021 10:38AM
for _ in range(int(input())):
  order = input()
  free, cost = 0, 0
  for o in order:
    if o in ['U','M']:
      if free > 0: free -= 1
      else: cost += 5
    else: free += 1 
  print(cost)
