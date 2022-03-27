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
# SOLUTION - 27/3/2022 10:29AM
N = int(input());
result = -1;
for num in range(10**(N-1), 10**N):
  count = 0;
  for i in [2, 3, 5, 7]:
    if num % i == 0:
      count += 1;
  if count == 4:
    result = num;
    break;
print(result);
