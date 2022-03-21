# Nishant again started a Business
'''
Nishant got bored after failing to solve competitive programming questions and again started a new business. 
This time Nishant started a shop for chocolates, he bought a lot of chocolates of the same value, 1 bronze coin. 
But soon he found out that children came with gold and silver coins and he has to provide the children the change 
otherwise he will be in a lot of trouble. 
But Nishant does not have any change left as he spent all his coins on buying chocolates.
1 gold coin = 4 bronze coins.
1 silver coin = 2 bronze coins.

Children come to Nishant in order and hand him a coin and he has to provide him the chocolate and the change.
Help Nishant finds that will he be able to provide the children with sufficient change or not. 

Note: 
1 stands for the bronze coin, 
2 for silver and 
4 for a gold coin.

Input format
First-line contains an integer T where T is number of test cases.
For every Test case:
The next line contains one integer N representing the number of children that came to Nishant's shop.
The next line contains N integers the coins bought by children. 

Output format
For every test case print Yes or No according to the above-mentioned conditions.  

Constraints
. 1 <= T <= 70
. 1 <= N <= 10^5

Time Limit
1 second

Example
Input
1
3 
1 1 2

Output
Yes

Explanation
Nishant has got two bronze coins from 1st two children, now he can take the silver coin 
from 3rd child and give him one bronze coin and the chocolate.
'''
# SOLUTION - 22/3/2022 2:29AM
for _ in range(int(input())):
    N = int(input());
    coins = list(map(int, input().split()));
    count = [0, 0, 0]; result = 'Yes';
    for i in range(N):
        c = coins[i];
        if c == 1:
            count[0] += 1;
        elif c == 2:
            if count[0] >= 1:
                count[1] += 1;
                count[0] -= 1;
            else:
                result = 'No';
                break;
        else:
            if count[0] >= 1 and count[1] >= 1:
                count[1] -= 1;
                count[0] -= 1;
            elif count[0] >= 3:
                count[0] -= 3;
            else:
                result = 'No';
                break;
            count[2] += 1;
    print(result);
