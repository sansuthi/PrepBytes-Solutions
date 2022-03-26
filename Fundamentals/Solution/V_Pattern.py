# V Pattern
'''
Print in the output the exact pattern provided below
1        1
12      21
123    321
1234  4321
1234554321

Input format
A single character denoted by ch

Output format
Print the same pattern provided in the problem statement.

Constraints
. ch = ′V′

Time Limit
 1 second 

Input
V

Output
1        1
12      21
123    321
1234  4321
1234554321
'''
# SOLUTION - 26/3/2022 7:59PM
ch = input();
x = 8;
for i in range(1, 6):
    n = 0;
    while n < i:
        n += 1;
        print(n, end=''); 
    print(' ' * x, end='');
    while n >= 1:
        print(n, end='');
        n -= 1;   
    x -= 2;
    print();
