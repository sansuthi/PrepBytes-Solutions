# New Office
'''
PrepBytes has opened a new office having N floors in it called the 1st floor through Nth floor and each floor has K rooms called the 
1st room through Kth room. Here both N and K are single-digit integers and the jth room on the ith floor has the room number i0j.

For Example, the 3rd room on the 2nd floor has room number 203.

Prepbudy appointed as new manager interested in the sum of room numbers of all rooms in the office where each room number is seen as a 
three-digit integer. Find this sum.

Input format
The first line contains a single integer T - the number of test cases.
The first line of the test case contains two space-separated integers N and K - the number of floors in the office and the number of 
rooms on each floor.

Output format
For each test case print a single integer - the sum of all room numbers in the office.

Constraints
. 1 ≤ T ≤100
. 1 ≤ N, K ≤ 9

Example
Sample Input
1
1 2

Sample Output
203

Explanation
For this test case The office has two rooms 101 and 102 so we have sum = 101 + 102 = 203.
'''
# SOLUTION - 28/9/2021 6:02PM
for _ in range(int(input())):
  n, k = map(int, input().split())
  floor_sum = 0
  for i in range(1, n+1):
    for j in range(1, k+1):
      floor_sum += (i * 100) + j
  print(floor_sum)
