# Check Palindrome
'''
Given a number N, check whether the number is palindrome or not, using recursion. 
The palindrome number remains the same when its digits are reversed.

Input Format
The first line contains an integer T, denoting the number of test cases.
For each test case, there is only one input, an integer N.

Output Format
For each test case, on a new line print YES if the given number is palindrome else print NO.

Constraints
. 1 <= T <= 10
. 1 <= N <= 10^5

Time Limit
1 second

Example
Input
3
234
121
14141

Output
NO
YES
YES

Sample test case explanation
The reverse of 234 is 432, and they are not the same, so the answer is NO.
The reverse of 121 is 121, and they are the same, so the answer is YES.
'''
# SOLUTION - 21/3/2022 12:56AM
def palindrome(num, n_sum=0):
    if num == 0:
        return n_sum
    else:
        return palindrome(num//10, (n_sum*10)+(num%10))

for _ in range(int(input())):
    number = int(input())
    if number == palindrome(number):
      print('YES')
    else:
      print('NO')
