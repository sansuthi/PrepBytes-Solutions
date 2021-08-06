# Toppers
'''
In a class, we have three toppers Hari, Ram, and Krishna. The students of the class stand in a row where Hari, Ram, and 
Krishna are the first 3 students. The teacher asks every student of the class to choose a number randomly. All the students 
except the toppers cheat, the students choose their number by adding the number chosen by the previous 3 students. You are 
given the number chosen by Hari, Ram, and Krishna. You have to find all the numbers chosen by n students.

Input format
First line contains integer t, denoting number of testcases. Next t lines, each contains four integers a, b, c, n.

Output format
Print t number of lines, where each line contains n integers.

Constraints:
1 <= t <= 100
3 <= n <= 20
1 <= a, b, c <= 10

Example
Input
2
1 2 3 5
9 4 3 7

Output
1 2 3 6 11 
9 4 3 16 23 42 81 

Sample test case explanation
In the first test case first 3 scores are 1 2 and 3, therefore 4th score is 1+2+3=6 and fifth score is 6+3+2=11.
'''
# SOLUTION - 31/7/2021 9:51PM
for _ in range(int(input())):
  array = list(map(int, input().split()))
  l = array[-1]
  array.pop()
  for i in range(l-3):
    array.append(sum(array[i:i+3]))
  print(*array)
