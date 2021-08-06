# Fix it
'''
N students are lined up in a row and some of the students are in standing state and some of them are in sitting state. 
Priya is the class representative and her sports teacher told her that he needs exactly N/2 students to stand up and the 
others to sit down. In one minute, Priya can make some students sit down or stand up.Calculate the minimum number of students 
Priya needs to change the state of to complete the task.

Input Format
The first line of input contains an integer T, denoting the number of test cases.
The first line of each test case contains a string S, of length N consisting of characters 'U'(i.e student is standing) 
and 'D'(i.e student is sitting).

Output Format
For each test case on a new line, print the minimum number of students Priya needs to change the state of to complete the task.

Constraints
. 1 ≤ T ≤10
. 2 ≤ N ≤105
. N is even


Example
Input
2
DDUD
UDUDUD

Output
1
0
'''
# SOLUTION - 5/8/2021 8:25PM
for _ in range(int(input())):
  array = list(input())
  print(abs((len(array)//2) - array.count('U')))
