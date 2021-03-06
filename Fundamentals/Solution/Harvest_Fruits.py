# Harvest Fruits
'''
There are N trees and ith tree bears Ai fruits. Prepbudy will harvest fruits from the trees in the following manner.
From a tree with 10 or fewer fruits he does not take fruits. From a tree with more than 10 fruits, he takes all of the 
fruits if the number of fruits in that tree is odd else if the number of fruits in that tree is even then he takes half of it.
Since prepbudy is busy harvesting fruits he asks you to find the maximum number of fruits he can take from all the trees present.

Input format
The first line of input contains a single integer T - the number of test cases.
The first line of the test case contains a single integer N - the number of trees.
The next line of each test contains N space-separated integers A1, A2....AN where Ai denotes the number of fruits in the ith tree. 

Output format
For each test case print a single integer - the maximum number of fruits Prepbudy can take from all the trees.

Constraints
. 1 ≤ T ≤ 100
. 1 ≤ N ≤ 2∗10^5
. 1 ≤ Ai ≤ 2∗10^5

Time Limit
1 second

Example
Sample Input
1
3
6 17 28

Sample Output
31
'''
# SOLUTION - 27/3/2022 10:08AM
for _ in range(int(input())):
    N = int(input());
    fruits = list(map(int, input().split()));
    total = 0;
    for f in fruits:
        if f > 10:
            if f % 2 != 0:
                total += f;
            else:
                total += f//2;
    print(total);
