# Find Median
'''
Arnab is given two sorted arrays of length n and length m. Help Arnab to find the median of two arrays after they are merged.
The catch is that it is not allowed to use extra space or merge the two arrays into one single array and find the median.

Expected Complexity: O(log(m+n))

Input format
First line contains integer t, number of testcase. For each testcase:
The first line contains two integers n and m.
The second line contains n space seperated integers.
The third line contains m space seperated integers.

Output format
For each testcase print the median
In case of m+n= odd, mid element is median.
In case of m+n= even, average of two mid elements is the median(double value).

Constraints:
. 1 <= t <= 10
. 1 <= n, m <= 10^5

Example
Input
1
2 3
1 2
3 4 5

Output
3

Sample test case explanation
Array1 = [1,2]
Array2 = [3,4,5]
Merged array would be [1,2,3,4,5]
Median = 3
'''
# SOLUTION - 5/9/2021 9:48AM
for _ in range(int(input())):
  n, m = map(int, input().split())
  array = sorted(list(map(int, input().split())) + list(map(int, input().split())))
  if (m+n) % 2 == 0: print(sum(array[((m+n)//2)-1:((m+n)//2)+1])/2)
  else: print(array[(m+n)//2])
