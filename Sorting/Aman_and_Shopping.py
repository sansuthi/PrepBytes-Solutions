# Aman and Shopping
'''
Aman went to a shopping mall. There are N items in the shopping mall and each item has some price. The ith item has 
Ai price. He has only X rupees and he wants to buy maximum items in X rupees, the condition is that he cannot buy 
more than one item of the same cost. You have to find how many items Aman can buy.
Note: He can't buy more than N items.

Input format
The first line contains an integer T- denoting the number of test cases. 
For each test case:-
The first line of the input contains two integers N and X, where N is denoting the number of items and X is denoting the rupees.
The second line of the input contain N integer, A1,A2,A3,....AN space-separated,  Ai denoting the price of ith item.

Output format
For each test case, print a single integer - The maximum number of unique price items Aman can buy in X rupees.

Constraints
1 <= T <= 10
1 <= N, X <= 10^5
1 <= Ai <= 10^4

Example
Input
2
8 10
4 2 5 1 6 8 7 3
5 10
1 2 3 3 3

Output
4
3

Sample test case explanation
Test case 1:-
Input: price of 8 item is [4, 2, 5, 1, 6, 8, 7, 3]
value of X = 10
Aman can buy these items:
 item number  price of item
       1       4
       2       2
       4       1
       8       3
Total price of 4 items is 4 + 2 + 1 + 3 = 10
So Aman can buy maximum 4 items.
'''
# SOLUTION - 31/7/2021 3:10PM
for _ in range(int(input())):
  n, total = map(int, input().split())
  array = sorted(set(map(int, input().split())))
  k = 0
  item = 0
  for ar in array:
    k += ar
    if k <= total:
      item += 1
    else:
      break
  print(item)
