# Unique Frequencies
'''
You are given an array A of N integers. The task is to determine if the value of frequency of each element in the array is unique.

Input Format
The first line of input contains a single integer T - denoting the number of test cases.
Each test case follows:
. The first line of each test case contains a single integer N.
. The second line contains N space-separated integers.

Output Format
Print "Yes" (without quotes) if all elements have a unique frequency. Else print "No" (without quotes). 
Display output for each test case in a new line.

Constraints
. 1 ≤ T ≤ 100
. 1 ≤ N ≤ 2∗10^4
. 1 ≤ Ai ≤ 10^4

Examples
Input
2
6
5 6 7 7 6 6
5
1 2 3 4 2

Output
Yes
No

Sample Test Case Explanation
For the first test case:
Frequency of 5: 1
Frequency of 6: 3
Frequency of 7: 2
All elements have a unique frequency.
So the answer is Yes.

For the second test case:
Frequency of 1: 1
Frequency of 2: 2
Frequency of 3: 1
Frequency of 4: 1
Frequencies of 1, 3, 4 are same.
So the answer is No.
'''
# SOLUTION - 20/8/2021 11:42AM
for _ in range(int(input())):
  n = input()
  array = list(map(int, input().split()))
  count = [array.count(ar) for ar in set(array)]
  print('Yes') if len(set(count)) == len(count) else print('No')
