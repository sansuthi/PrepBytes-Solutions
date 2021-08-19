# Prime Number
'''
You have given only these prime numbers 2, 3, 5 and 7. You have to find the minimum number of length N, such that it is 
simultaneously divisible by all given prime numbers (2, 3, 5 and 7). A number's length is the number of digits in its 
decimal representation without leading zeros.

Input Format
A single input line contains a single integer N.

Output Format
Print a single integer — the answer to the problem without leading zeroes, or "-1" (without the quotes), if the number 
that meets the problem condition does not exist.

Constraints
. 1 ≤ N ≤ 10^6

Examples
Input1
2
Output1
-1

Input2
6
Output2
100170
'''
# SOLUTION - 19/8/2021 9:47AM
n = int(input())
for num in range(10**(n-1), 10**(n)):
  count = [1 for i in [2, 3, 5, 7] if num % i == 0]
  if sum(count) == 4:
    print(num)
    break
else: print(-1)
