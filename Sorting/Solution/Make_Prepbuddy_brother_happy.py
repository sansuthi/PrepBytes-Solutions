# Make Prepbuddy's brother happy
'''
Prepbuddy's younger brother is angry because Prepbuddy is not giving the phone to him to play the famous game PUBG. 
So, to make him happy Prepbuddy went to a shop to buy exactly K candies. There are N types of candies in the shop. 
Prepbuddy wants K candies each of the different type. Every type of candy has a happiness value Ai(1<=i<=N). 
Prepbuddy wants to choose K different type of candies in such a way that the sum of happiness values of candies is 
maximum possible so that he can make his brother happy.

Input format
The first line contains two integers N and K separated by space.
The second line contains N space-separated integers, denoting the happiness values of chocolates.

Output format
Print the maximum sum of happiness values of K candies of different types.

Constraints
1 <= K <= N <= 2∗10^5
1 <= Ai <= 10^6

Example
Input
5 3
4 7 1 2 8

Output
19

Sample test case explanation
For K=3, we can choose candies with happiness values 7,8, and 4 so the total sum will be 7+8+4=19.
'''
# SOLUTION - 31/7/2021 6:40PM
N, K = map(int, input().split())
array = sorted(list(map(int, input().split())), reverse=True)
print(sum(array[:K]))
