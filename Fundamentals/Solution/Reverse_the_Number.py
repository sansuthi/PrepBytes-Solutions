# Reverse the number
'''
PrepBuddy gave you a number X and asks you to reverse that number and print it.

Input format
One integer is provided denoting the value of X.
Note - The given number doesn't have leading or ending zero's.

Output format
Print the reverse of X.

Constraints
1 <= X <= 10^6

Example
Input
102345

Output
543201
'''
# SOLUTION - 27/3/2022 9:30AM
num = int(input());
rev = 0;
while num > 0:
    rev = rev*10 + num%10;
    num //= 10;
print(rev);
