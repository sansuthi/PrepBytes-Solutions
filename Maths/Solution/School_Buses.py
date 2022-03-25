# School Buses
'''
There is currently 1 bus in your school. The total strength of the school is N and the capacity of one bus is C. 
In order to carry all the students for the trip the school will buy some more buses before the trip day. What is the 
total number of buses in the school on trip day if the school buys minimum number of buses enough to carry all the students.

Input Format
The first line contains T, the number of test cases.
The next T lines contains two space separated integers N and C each.

Output Format
For each test case, print on new line the total number of buses on the day of trip for that test case.

Time Limit
1 second

Constraints
. 1 ≤ T ≤ 10^5
. 0 ≤ N ≤ 10^9
. 1 ≤ C ≤ 10^9

Example
Sample Input
3
10 4
5 5
7 9
Sample Output
3
1
1

Sample test case explanation
In the first test case, 2 new buses will be bought so there will be 3 in total.
In the second test case, no new bus will be bought since the existing bus can carry 5 students, so there will be just 1 bus in total.
'''
# SOLUTION - 25/3/2022 11:14PM
for _ in range(int(input())):
  N, C = map(int, input().split());
  if N <= C:
    required = 1;
  elif N % C == 0:
    required = N // C;
  else:
    required = N // C + 1;
  print(required);
