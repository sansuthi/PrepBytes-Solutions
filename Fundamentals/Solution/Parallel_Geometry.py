# Parallel Geometry
'''
Manikya is a very keen child and has lots of interest in learning about geometric shapes. His father gifted him a box containing 
various sets of 12 sticks each and connectors using which he can construct and study about different geometric shapes in 3 dimension. 
After a week, his father decided to test Manikya's knowledge and asked him that given the height of the 12 sticks is it possible to 
create a parallelepiped using those 12 sticks or not. Manikya has to answer without actually trying to connect the 12 sticks. 
Help Manikya to find the answer.

Input Format
The first line contains an integer T denoting the number of test cases.
Each of the next T lines contains 12 space-separated integers denoting the height of sticks.

Output Format
For each test case on a new line print "yes" (without double quotes) if it is possible to construct a parallelepiped,
else print "no" (without double quotes).

Constraints
. 1 <= T <= 1000
. 1 <= height <= 10^9

Examples
Input
2
7 7 8 9 9 8 7 7 9 8 8 9
1 2 2 1 3 4 4 3 1 1 2 2

Output
yes
no
'''
# SOLUTION - 19/8/2021 6:36PM
for _ in range(int(input())):
  array = list(map(int, input().split()))
  count = len([1 for x in set(array) if array.count(x) % 4 == 0])
  print('yes') if count == len(set(array)) else print('no')
