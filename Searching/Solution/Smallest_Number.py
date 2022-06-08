# Smallest Number
'''
You are given an array a with N integers and an integer K. Output the smallest number in the array 
which occurs exactly K times in an array. There will always be a number that is occurring K times.

Input:
. First-line contains N, 
. The second line contains N space-separated integers. 
. The third line contains K.

Output
Print the smallest number in the array which occurs exactly K times in an array.

Constraints:
. 1 ≤ N ≤ 10^5
. 0 ≤ a[i] ≤ 10^5
. 1 ≤ K ≤ 10^5
 
Time Limit
1 second

Sample Input
5
2 2 1 3 1
2

Sample Output
1
'''
# SOLUTION - 8/6/2022 6:51PM
N = int(input());
a = list(map(int, input().split()));
K = int(input());
counts = {};
for i in range(N):
  c = a[i];
  if c not in counts:
    counts[c] = 0;
  counts[c] += 1;
numbers = [];
for num in counts:
  if counts[num] == K:
    numbers.append(num);
print(min(numbers));
