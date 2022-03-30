# Get the Sun Light
'''
The sun is out and you are given an array containing unique integers representing height of buildings in a 
society and the arrangement looks something like this in the image.

_______________________________________________________
|                                                      |
|                                                      |
|                                                      |
|  sun                                     ___         |
|                                         |   |        |                
|               ___                       |   |        |
|              |   |     Buildings        |   |        |
|              |   |     ___              |   |        |
|              |   |    |   |             |   |        |
|              |   |    |   |             |   |        |
|              |   |    |   |     ___     |   |        |              
|              |   |    |   |    |   |    |   |        |
|              |   |    |   |    |   |    |   |        |
|              |   |    |   |    |   |    |   |        |
|              |   |    |   |    |   |    |   |        |
 _______________________________________________________

The sun faces building from left to right. Your task is to find out the number of buildings facing the sun.

Input
First line contains an integer T, number of test cases. 
Then follows T test cases. Each test case consists of two lines. 
First line contains an integer N denoting the number of buildings. 
Second line contains N space separated integers Hi denoting height of the buildings.

Output
Print T lines, each containing count of buildings facing the sun.

Constraints
. 1 <= T <= 100
. 1 <= N <= 10^6
. 0 <= Hi <= 10^8

Time Limit
1 second

Example
Input
2
5
7 4 8 2 9
4
2 3 4 5

Output
3
4

Sample test case explanation
In the first test case
1. Building with a height of 7 is receiving the sunlight.
2. Building with a height of 4 is not receiving the sunlight 
   because it is blocked by a higher building with height = 7.
3. Building with a height of 8 is receiving the sunlight.
4. Building with a height of 2 is not receiving the sunlight 
   because it is blocked by a higher building with height = 8.
5. Building with a height of 9 is receiving the sunlight.
'''
# SOLUTION - 30/3/2022 2:13PM	
for _ in range(int(input())):
  N = int(input());
  H = list(map(int, input().split()));
  max_height = H[0]; count = 1;
  for i in range(1, N):
    if H[i] > max_height:
      max_height = H[i];
    if H[i] >= max_height:
      count += 1;
  print(count);
