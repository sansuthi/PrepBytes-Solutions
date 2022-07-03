# Toy Cupboard
'''
Pragya has two types of toys, Animal figure toys, and Bird figure toys. More specifically she has d1 dog toys, 
c1 cat toys and m1 mouse toys in her Animal toys collection and p1 parrot toys, s1 sparrow toys and k1 kiwi toys 
in her Bird toys collection. Her father brought her a cupboard with N shelves and she decided to put are toys on 
these N shelves. She wants to classify between her toys and also shelves should not look messy. That's why Pragya 
decided to follow these rules.
. any shelf cannot contain both Animal and Birds toys at the same time.
. no shelf can contain more than five Animal toys
. no shelf can have more than ten Bird toys.
Help Pragya to find out if she can put all the toys on the shelves such that all the conditions are fulfilled.

Input format
First line contains 3 integers denoting values of d1, c1 and m1 respectively.
Second line contains 3 integers denoting values of p1, s1 and k1 respectively.
Third line contains one integer representing the value of N.

Output format
For each test case, print YES if all the toys can be placed on the shelves in the described manner, otherwise print NO.

Constraints
. 0 <= d1, c1, m1 <= 100
. 0 <= p1, s1, k1 <= 100
. 1 <= N <= 100

Time Limit
1 second 

Example
Input
1 2 3
2 4 6
3

Output
NO
'''
# SOLUTION - 3/7/2022 10:31AM
d, c, m = map(int, input().split());
p, s, k = map(int, input().split());
N = int(input());
anim = d + c + m;
bird = p + s + k;
required = anim//5 + bird//10;
if anim % 5 != 0:
    required += 1;
if bird % 10 != 0:
    required += 1; 
if required > N:
    print('NO');
else:
    print('YES');
