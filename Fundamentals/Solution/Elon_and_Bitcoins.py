# Elon and Bitcoins
'''
Elon is the CEO of Tesla. He is a very genius person who can change the position of the stock market with just a single tweet. 
He recently tweeted that his company "Tesla" can take the payment in bitcoins also. Bitcoin is a very popular cryptocurrency 
that is in the market from 2008. A guy named Satoshi Nakamoto wants to buy a premium Tesla Car. For buying the car, he paid 
N bitcoins to the company. But, now Elon is facing a problem. The problem is, due to certain protocols over the collection of 
bitcoins, he can not store all these bitcoins together. So, he wants to group these bitcoins in such ways that no bitcoin is 
alone in the group and each group has the same number of bitcoins.

So, your task is to help your friend Elon in solving this complex problem by telling the possible number of ways to divide the 
bitcoins into groups such that no bitcoin is alone in the group and each group have the same number of bitcoins

Input Format
The input consists of a single line containing a positive integer N, denoting the number of bitcoins.

Output Format
Print a single integer representing the number of ways he can divide the bitcoins according to the problem.

Constraints
. 1 ≤ N ≤ 10^5

Example
Sample Input
10

Sample Output
3

Explanation
2 + 2 + 2 + 2 + 2 = 10
5 + 5 = 10
10 = 10

So, we have 3 ways to divide the bitcoins.
'''
# SOLUTION - 27/3/2022 9:51AM
coins = int(input());
count = 0;
for i in range(2, coins+1):
    if coins % i == 0:
        count += 1;
print(count);
