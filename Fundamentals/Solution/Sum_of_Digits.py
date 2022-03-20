# Sum of Digits
'''
PrepBuddy gave you a number X and asks you to find the sum of the digits present in the number.

Input format
One integer is provided denoting the value of X.

Output format
Print the sum of digits of X.

Constraints
. 1 <= X <= 10^6

Time Limit
1 second

Example
Input
102345

Output
15

Sample test case explanation
Sum of digit = 1 + 0 + 2 + 3 + 4 + 5 = 15
'''
# SOLUTION - 20/3/2022 10:17PM
number = int(input())
digit_sum = 0
while number != 0:
    digit_sum += number%10
    number //= 10
print(digit_sum)
