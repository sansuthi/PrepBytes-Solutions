# Boxes and Toys
'''
Tina and Rahul have 1 toy each. They are entering into an amusement park but it is not allowed to take the toys inside, 
so they have to keep it in the boxes provided by the park management. They want to keep the toys together in one box. 
There are N boxes in total, at this moment there are ti toys present in ith box and the maximum capacity of the box is 
denoted by ci. Rahul and Tina want to know in how many boxes can they keep their toys such that both the toys are in the 
same box.

Input format
The first line of the input contains integer N, denoting the count of boxes. Each of the next N lines contains two integers 
ti and ci denoting the number of toys present in the ith box and the maximum capacity of that box.

Output format
Print the maximum number of boxes that fulfill the conditions.

Constraints
1 <= N <= 100
0 <= ti, ci <= 100

Example
Input
4
1 2
2 4
5 6
6 10

Output
2
'''
# SOLUTION - 30/7/2021 11:59PM
cap = 0
for _ in range(int(input())):
  t, c =  map(int, input().split())
  if abs(t-c) >= 2:
    cap += 1
print(cap)
