# Book Sales
'''
Once Prepbudy is gone to a book sales. There were N books in the stall. Book with index i costs Pi. Some books have a negative 
price - their owners are ready to pay Prepbudy if he buys their very old book. But the sales have a rule that Prepbudy can buy 
at most M books. Prepbudy is busy buying the books to help him to find the maximum amount of money he gets from the sale.
Note: It is possible that Prepbudy does not buy any book.

Input Format
The first line of the input contains a single integer T - the number of test cases.
The first line of each test case contains two space-separated integers N - the number of books in the sale and M denoting 
the maximum number of books Prepbudy can buy.
The next line contains N space-separated integers P1,P2.....PN - the price of the ith box.

Output Format
For each test case print, a single integer - the maximum amount of money Prepbudy can get from the sale.

Constraints
1 ≤ T ≤ 10^2
1 ≤ N, M ≤ 10^4

−10^3 ≤ Pi ≤ 10^3

Example
Sample Input
3
5 3 
-6 0 35 -2 4
4 2 
7 0 0 -7
3 2
1 2 3

Sample Output
8
7
0

Sample Testcase Explanation
In the first test case if Prepbudy buys books with index [1,2,4] then he can get the maximum amount i.e. 8.
'''
# SOLUTION - 31/7/2021 2:04PM
for _ in range(int(input())):
  books, num = map(int, input().split())
  array = sorted(list(map(int, input().split())))[:num]
  result = [-i if i < 0 else 0 for i in array]
  print(sum(result))
