# Sum of Sequence
'''
You are given a positive integer N. Your task is to make a recursive function and sum all the number until 
N reaches to 1 after performing the following two operations:-

. If N is even, then N = N/2
. If N is odd, then N = 3∗N + 1
Repeat the above steps, until N becomes 1.

Note:- It is guaranteed that after performing the above two operations N will become 1 at some point
Note:- Sum of all number can be large, so print the answer with modulo (10^9 + 7)

Note:-  - In real interviews, you have to use recursion when asked by the interviewer. So the coins will not be 
awarded if the solution is not recursive in the contest.

Input Format
The first line contains an integer T denoting the number of test cases. 
For each test case: an integer N is provided.

Output Format
For each test case print, the output in the new line: The sum all number until N reaches to 1 (including 1).

Constraints
. 1 <= T <= 10^2
. 1 <= N <= 10^6

Time limit
1 second

Example
Input
2
4
5

Output
7
36

Sample test case explanation
Test case 1:
Input: N=4
The sequance will be [4, 2, 1], sum = 4 + 2 + 1 
Output: 7

Test case 2:
Input: N=5
The sequance will be [5, 16, 8, 4, 2, 1], sum = 5 + 16 + 8 + 4 + 2 + 1  
Output: 36
'''
# SOLUTION - 22/3/2022 2:26AM
def sequence(number, seq_sum=0):
    seq_sum += number;
    if number == 1:
        return seq_sum % (10**9+7);
    if number % 2 == 0:
      	return sequence(number//2, seq_sum);    
    else:
      	return sequence((number*3)+1, seq_sum);
    
for _ in range(int(input())):
    print(sequence(int(input())));
